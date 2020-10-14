from typing import List, Dict, Any, Optional, Union
from enum import Enum
from datetime import datetime

from fastapi import status, HTTPException

from app.payloads.query_builder import FactoryQueryBuilder
from ..db.mongodb import AsyncIOMotorClient
from ..core.config import database_name, analyze_collection
from ..models.notes import NoteCreate, NoteSchema, fix_item_id, NoteUpdate, NoteInDb, PriorityEnum
from ..models.users import UserSchema 
from bson.objectid import ObjectId


async def post(conn: AsyncIOMotorClient, payload: NoteCreate, current_user: UserSchema) -> NoteSchema:
    payload.owner = current_user.id
    result = await conn[database_name][analyze_collection].insert_one(payload.dict())
    note = await conn[database_name][analyze_collection].find_one({"_id": result.inserted_id})
    
    return NoteSchema(**note)


async def get(id_: str, conn: AsyncIOMotorClient, current_user: UserSchema) -> NoteSchema:
    try:
        return NoteSchema(**await conn[database_name][analyze_collection].find_one({"$and": [{"_id": ObjectId(id_), "owner": current_user.id}]}))
    except TypeError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note Not Found")


async def get_all(
    conn: AsyncIOMotorClient, 
    filters: Dict[str, Optional[Union[str, int, List[str]]]], 
    current_user: UserSchema
) -> List[NoteSchema]:
    if not any(filters.values()):
        cursor = conn[database_name][analyze_collection].find({"owner": current_user.id}).sort('_id')
        notes = [document async for document in cursor]
        return sorted(notes, key=lambda note: (note['priority'], note['due_at']))
    else:
        only_active_filters: Dict[str, Union[str, int, List[str]]] = {item[0]: item[1] for item in list(filter(lambda item: item[1] is not None, filters.items()))}
        only_active_filters['note_owner'] = current_user.id
        query_build = FactoryQueryBuilder.query_build(only_active_filters)
        cursor = conn[database_name][analyze_collection].aggregate([{"$match": {"$and": query_build}}])

        return [document async for document in cursor]


async def put(id_: str, payload: NoteUpdate, conn: AsyncIOMotorClient, current_user: UserSchema) -> NoteSchema:
    payload.modified_at = datetime.utcnow().isoformat()

    updated_note = await conn[database_name][analyze_collection].find_one_and_update(
        filter={"$and": [{"_id": ObjectId(id_), "owner": current_user.id}]}, 
        update={"$set": payload.dict(exclude={"created_at"}, exclude_none=True, exclude_defaults=True)},
        return_document=True
        )
    if updated_note:
        return NoteSchema(**updated_note)
    else:
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED)


async def delete(id_: str, conn: AsyncIOMotorClient, current_user: UserSchema):
    delete_result = await conn[database_name][analyze_collection].delete_one({"$and": [{"_id": ObjectId(id_), "owner": current_user.id}]})
    if not delete_result.deleted_count:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note Not Found")



async def do_delete_many(conn: AsyncIOMotorClient) -> List[NoteSchema]:
    n = await conn[database_name][analyze_collection].count_documents({})
    print('%s documents before calling delete_many()' % n)
    result = conn[database_name][analyze_collection].delete_many({})
    print('%s documents after' % (await conn[database_name][analyze_collection].count_documents({})))
