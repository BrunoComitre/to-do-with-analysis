from typing import List, Dict, Optional, Union
from datetime import datetime
from bson import ObjectId

from fastapi import status, HTTPException

from app.payloads.query_builder import FactoryQueryBuilder
from ..db.mongodb import AsyncIOMotorClient
from ..core.config import database_name, analyze_collection
from ..models.orders import (
    OrderCreate,
    OrderSchema,
    OrderUpdate,
)
from bson.objectid import ObjectId


async def post(conn: AsyncIOMotorClient, payload: OrderCreate) -> OrderSchema:
    result = await conn[database_name][analyze_collection].insert_one(payload.dict())
    order = await conn[database_name][analyze_collection].find_one(
        {"_id": result.inserted_id}
    )

    print(f"order >> {order}")

    return OrderSchema(**order)


async def get(id_: str, conn: AsyncIOMotorClient) -> OrderSchema:
    try:
        result = await conn[database_name][analyze_collection].find_one(
            {"$and": [{"_id": ObjectId(id_)}]}
        )

        if int(result["age"]) >= 18 and int(result["value"]) <= 10000000:
            return OrderSchema(**result)
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Order Não Corresponde por ser maior de Idade ou Saldo acima do Permitido",
            )
    except TypeError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Order Não Encontrada"
        )


async def get_all(
    conn: AsyncIOMotorClient,
    filters: Dict[str, Optional[Union[str, int, List[str]]]],
) -> List[OrderSchema]:
    if not any(filters.values()):
        cursor = conn[database_name][analyze_collection].sort("_id")
        orders = [document async for document in cursor]
        return sorted(orders, key=lambda order: (order["priority"], order["due_at"]))
    else:
        only_active_filters: Dict[str, Union[str, int, List[str]]] = {
            item[0]: item[1]
            for item in list(filter(lambda item: item[1] is not None, filters.items()))
        }
        query_build = FactoryQueryBuilder.query_build(only_active_filters)
        cursor = conn[database_name][analyze_collection].aggregate(
            [{"$match": {"$and": query_build}}]
        )

        return [document async for document in cursor]


async def put(id_: str, payload: OrderUpdate, conn: AsyncIOMotorClient) -> OrderSchema:
    payload.modified_at = datetime.utcnow().isoformat()

    updated_order = await conn[database_name][analyze_collection].find_one_and_update(
        filter={"$and": [{"_id": ObjectId(id_)}]},
        update={
            "$set": payload.dict(
                exclude={"created_at"}, exclude_none=True, exclude_defaults=True
            )
        },
        return_document=True,
    )
    if updated_order:
        return OrderSchema(**updated_order)
    else:
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED)


async def delete(id_: str, conn: AsyncIOMotorClient):
    delete_result = await conn[database_name][analyze_collection].delete_one(
        {"$and": [{"_id": ObjectId(id_)}]}
    )
    if not delete_result.deleted_count:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note Not Found"
        )


async def do_delete_many(conn: AsyncIOMotorClient) -> List[OrderSchema]:
    n = await conn[database_name][analyze_collection].count_documents({})
    print("%s documents before calling delete_many()" % n)
    result = conn[database_name][analyze_collection].delete_many({})
    print(
        "%s documents after"
        % (await conn[database_name][analyze_collection].count_documents({}))
    )
