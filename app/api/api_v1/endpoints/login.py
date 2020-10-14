from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.core.security import create_access_token, get_password_hash
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.models.token import Token
from app.db.mongodb import AsyncIOMotorClient, get_database
from app.payloads.users import authenticate


router = APIRouter()


@router.post("/login/access-token/", response_model=Token)
async def login_access_token(
    db: AsyncIOMotorClient = Depends(get_database), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = await authenticate(
        db, email=form_data.username, plain_password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    # elif not crud.user.is_active(user):
    #     raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": create_access_token(
            user['_id'], expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }