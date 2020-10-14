from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError

from app.core.config import ALGORITHM, API_V1_STR, SECRET_KEY
from app.db.mongodb import AsyncIOMotorClient, get_database
from app.models.users import UserSchema
from app.models.token import TokenPayload
from app.payloads.users import get_user

oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{API_V1_STR}/login/access-token"
)


async def get_current_user(
    db: AsyncIOMotorClient = Depends(get_database), token: str = Depends(oauth2)
) -> UserSchema:
    try:
        payload = jwt.decode(
            token, SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError) as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    # user = crud.user.get(db, id=token_data.sub)
    user = await get_user(token_data.sub, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user