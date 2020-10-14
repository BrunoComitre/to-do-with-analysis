from typing import List

from fastapi import APIRouter, HTTPException, Depends, status

from app.payloads import users
from app.models.users import UserSchema, UserUpdateSchema, UserCreateSchema
from ....db.mongodb import AsyncIOMotorClient, get_database


router = APIRouter()

@router.post("/users/", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def create_user(*, db:AsyncIOMotorClient = Depends(get_database), payload: UserCreateSchema):
    """[summary]
    Create user.

    [description]
    Endpoint to retrieve an specific define create user.
    """
    return await users.create(db, payload)


@router.get("/users/{user_id}/", response_model=UserSchema)
async def get_user(user_id:str, db:AsyncIOMotorClient = Depends(get_database)):
    """[summary]
    Return user by ID.

    [description]
    Endpoint to retrieve an specific user.
    """
    return await users.get_user(user_id, db)


@router.get("/users", response_model=List[UserSchema])
async def get_all_users(db: AsyncIOMotorClient = Depends(get_database)):
    """[summary]
    Get all users by ID.

    [description]
    Endpoint to retrieve an specific item.
    [optional]
    """ 
    return await users.get_all_users(db)
