from fastapi import APIRouter, HTTPException, Depends, status

from app.payloads import gensim
from app.models.gensim import DocumentSchema, fix_item_id
from app.models.notes import NoteSchema, fix_item_id
from ....db.mongodb import AsyncIOMotorClient, get_database


router = APIRouter()


@router.get("/corpus")
async def view_corpus(db: AsyncIOMotorClient = Depends(get_database)):
    """[summary]
    Return text corpus.

    [description]
    Endpoint to retrieve an specific item.
    """  
    corpus = await gensim.return_all(db)

    if not corpus:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notes not exist!")    

    return corpus

@router.post("/document_analyzed/", status_code=status.HTTP_201_CREATED)
async def document_analyze(*, db:AsyncIOMotorClient = Depends(get_database), payload: NoteSchema):
    """[summary]
    View inserts item in the document string.

    [description]
    Endpoint to retrieve an specific item.
    """

    analyze = await gensim.result(db, payload)
    return fix_item_id(analyze)
