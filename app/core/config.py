import secrets
import os
import urllib.parse

from dotenv import load_dotenv
from starlette.datastructures import CommaSeparatedStrings
from databases import DatabaseURL

from urllib.parse import quote_plus
from pydantic import BaseSettings


API_V1_STR = "/api"

load_dotenv(".env")

MAX_CONNECTIONS_COUNT = int(os.getenv("MAX_CONNECTIONS_COUNT", 10))
MIN_CONNECTIONS_COUNT = int(os.getenv("MIN_CONNECTIONS_COUNT", 10))

SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"

PROJECT_NAME = os.getenv("PROJECT_NAME", "FastAPI example application")
ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv("ALLOWED_HOSTS", ""))

ACCESS_TOKEN_EXPIRE_MINUTES = 10

MONGODB_URL = os.getenv("MONGODB_URL", "")  # deploying without docker-compose

username = urllib.parse.quote_plus("username")
password = urllib.parse.quote_plus("password")


if not MONGODB_URL:
    MONGO_HOST = os.getenv("MONGO_HOST", "mongodb")
    MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
    MONGO_USER = os.getenv("MONGO_USER", "username")
    MONGO_PASS = os.getenv("MONGO_PASSWORD", "password")
    MONGO_DB = os.getenv("MONGO_DB", "development")
    MONGO_AUTH_SOURCE = os.getenv("MONGO_AUTH_SOURCE", "admin")

    MONGODB_URL = DatabaseURL(
        f"mongodb://{username}:{password}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?authSource={MONGO_AUTH_SOURCE}"
    )
else:
    MONGODB_URL = DatabaseURL(MONGODB_URL)

database_name = MONGO_DB
orders_collection = "orders"
analyze_collection = "smartresult"
gensim_collection = "gensimtestresult"
user_collection = "users"

STOPWORDS = """ de a o que e do da em um para é com não uma os no se na por mais
as dos como mas foi ao ele das tem à seu sua ou ser quando muito há nos já está
eu também só pelo pela até isso ela entre era depois sem mesmo aos ter seus quem
nas me esse eles estão você tinha foram essa num nem suas meu às minha têm numa
pelos elas havia seja qual será nós tenho lhe deles essas esses pelas este fosse
dele tu te vocês vos lhes meus minhas teu tua teus tuas nosso nossa nossos
nossas dela delas esta estes estas aquele aquela aqueles aquelas isto aquilo 
estou está estamos estão estive esteve estivemos estiveram estava estávamos
estavam estivera estivéramos esteja estejamos estejam estivesse estivéssemos
estivessem estiver estivermos estiverem hei há havemos hão houve houvemos
houveram houvera houvéramos haja hajamos hajam houvesse houvéssemos houvessem
houver houvermos houverem houverei houverá houveremos houverão houveria
houveríamos houveriam sou somos são era éramos eram fui foi fomos foram fora
fôramos seja sejamos sejam fosse fôssemos fossem for formos forem serei será
seremos serão seria seríamos seriam tenho tem temos tém tinha tínhamos tinham
tive teve tivemos tiveram tivera tivéramos tenha tenhamos tenham tivesse
tivéssemos tivessem tiver tivermos tiverem terei terá teremos terão teria
teríamos teriam again there about out very having with they own an be some for
do its yours such into of as most itself other is s am or who from me in each
the are we these your his through don nor more himself this down should our
their while off above both up to ours all when at any before them age same and
have will that because what over why so can did not now under where those i
after if theirs my against a by doing it was flows host request header content
type user content length host connection accept encoding body parsed header
query method mime type response header date expires cache control server mime
type gmt null gzip """
