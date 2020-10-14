from typing import List, Any
from bson.objectid import ObjectId
from collections import defaultdict
from gensim import corpora, models, similarities
from bson.objectid import ObjectId

from ..db.mongodb import AsyncIOMotorClient
from ..core.config import database_name, gensim_collection, analyze_collection, STOPWORDS
from ..models.gensim import DocumentSchema, fix_item_id
from ..models.notes import NoteSchema


async def return_all(conn: AsyncIOMotorClient) -> List[NoteSchema]:
    cursor = conn[database_name][analyze_collection].find({}).sort('_id')
    corpus = [document async for document in cursor]

    def filter_by(*field_names):
        for field_name in field_names:
            yield {field_name:[note[field_name] for note in corpus ] }

    await conn[database_name][gensim_collection].insert_one(
        {'filtered_notes': list(filter_by('title', 'description'))}
        )
    
    return list(filter_by('title', 'description'))

async def result(conn: AsyncIOMotorClient, payload: NoteSchema) -> NoteSchema:
    stoplist = set(STOPWORDS.split(' '))

    filtered_notes: dict = await conn[database_name][gensim_collection].find_one(
        {"_id": ObjectId('5f5f7924aa34788b1c19ff1e')}
        )

    # Inicializa o modelo tf-idf, treinando-o em nosso corpus e transformando a string
    words = "Tem o almoço janta lance café e leite bolacha e biscoito".lower().split()

    def filter_stopwords(notes):
        for words in notes:
            yield list(filter(lambda word: word not in stoplist, words.split() ))

    def tokenize(text_stopword):
        frequency = defaultdict(int)
        for text in text_stopword:
            for token in text:
                frequency[token] +=1
        return frequency

    def process_corpus(text_token, text_stopword):
        return [[token for token in text if text_token[token] > 1 ]
            for text in text_stopword]

    def dictionary(processed_corpus):
        dictionary = corpora.Dictionary(processed_corpus)
        dictionary_tokenized = dictionary.token2id
        return dictionary, dictionary_tokenized

    def note_analyze(new_note):
        return [word for word in new_note.lower().split() if word not in stoplist]

    def vectorize(dictionary, new_note, processed_corpus):
        new_vec = dictionary.doc2bow(str(new_note).lower().split())
        bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]
        tfidf = models.TfidfModel(bow_corpus)
        tf_idf = tfidf[dictionary.doc2bow(words)] 
        index_similarity = similarities.SparseMatrixSimilarity(tfidf[bow_corpus], num_features=7)  # Atualizar futuramente para quantidade presente em cada dicionário
        return bow_corpus, tfidf, index_similarity

    def query(dictionary_tokenized, query_document, index_similarity, tfidf):
        query_bow = dictionary_tokenized.doc2bow(query_document)
        sims = index_similarity[tfidf[query_bow]]
        return sims

    def result(sims):
        score_result = [list([int(document_number),float(score)]) for document_number, 
        score in sorted(enumerate(sims), key=lambda x: x[1], reverse=True)]
        result = {str(index): value for index, value in enumerate(score_result, 1)}
        return result

    titles: list = filtered_notes['filtered_notes'][0]['title']
    descriptions: list = filtered_notes['filtered_notes'][1]['description']

    texts_titles = list(filter_stopwords(titles))
    texts_descriptions = list(filter_stopwords(descriptions))

    titles_token = tokenize(texts_titles)
    description_token = tokenize(texts_descriptions)

    titles_corpus = process_corpus(titles_token, texts_titles)
    description_corpus = process_corpus(description_token, texts_descriptions)

    titles_dictionary = dictionary(titles_corpus)
    description_dictionary = dictionary(description_corpus)

    query_document_title = payload.dict()['title']
    query_document_description = payload.dict()['description']

    new_note_title = note_analyze(query_document_title)
    new_note_description = note_analyze(query_document_description)

    vectorize_title = vectorize(titles_dictionary[0], new_note_title, titles_corpus)
    vectorize_description = vectorize(description_dictionary[0], new_note_description, description_corpus)

    analyze_title = note_analyze(query_document_title)
    analyze_description = note_analyze(query_document_description)

    query_title = query(titles_dictionary[0], analyze_title, vectorize_title[2], vectorize_title[1])
    query_description = query(description_dictionary[0], analyze_description, vectorize_description[2], vectorize_description[1])

    result_title = result(query_title)
    result_description = result(query_description)
        
    result = dict(result_titles=result_title, result_descriptions=result_description)

    note_result = await conn[database_name][gensim_collection].insert_one(result) 
    result_id = await conn[database_name][gensim_collection].find_one({"_id": note_result.inserted_id})
    return fix_item_id(result_id)
