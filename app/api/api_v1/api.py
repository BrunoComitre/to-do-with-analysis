from fastapi import APIRouter

from .endpoints.notes import router as notes_router
from .endpoints.gensim import router as gensim_router
from .endpoints.users import router as users_router
from .endpoints.login import router as login_router


router = APIRouter()
router.include_router(notes_router, tags=['notes'])
router.include_router(gensim_router, tags=['analyze'])
router.include_router(users_router, tags=['users'])
router.include_router(login_router, tags=['login'])
