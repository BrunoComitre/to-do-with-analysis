from typing import List, Dict, Any, Optional, Union
from datetime import datetime
from bson.objectid import ObjectId

from ..db.mongodb import AsyncIOMotorClient
from ..core.security import verify_password, get_password_hash
from ..core.config import database_name, user_collection
from ..models.users import  UserCreateSchema, UserUpdateSchema, UserSchema


async def create(conn: AsyncIOMotorClient, payload: UserCreateSchema) -> UserSchema:
    payload.password = get_password_hash(payload.password)
    user_create =  await conn[database_name][user_collection].insert_one(payload.dict())
    return UserSchema(**payload.dict(), _id=user_create.inserted_id)

async def get_user(user_id: UserSchema, conn: AsyncIOMotorClient) -> UserSchema:
    user = await conn[database_name][user_collection].find_one({"_id": ObjectId(user_id)})
    if not user:
        return None
    return UserSchema(**user)

async def get_all_users(conn: AsyncIOMotorClient) -> List[UserSchema]:
    all_users_list =  conn[database_name][user_collection].find({})
    return [UserSchema(**user) async for user in all_users_list]

async def get_by_email(conn: AsyncIOMotorClient, email: str):
    return await conn[database_name][user_collection].find_one({"email": email})


async def authenticate(conn: AsyncIOMotorClient, *, email: str, plain_password: str) -> Optional[UserSchema]:
        user = await get_by_email(conn, email)
        if not user:
            return None
        if not verify_password(plain_password, user['password']):
            return None
        return user
