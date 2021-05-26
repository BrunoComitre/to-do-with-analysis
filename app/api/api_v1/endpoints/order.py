from typing import List, Optional
from fastapi import APIRouter, HTTPException, Depends, status

from app.payloads import orders
from app.models.orders import OrderCreate, OrderSchema, fix_item_id, OrderUpdate
from ....db.mongodb import AsyncIOMotorClient, get_database


router = APIRouter()


@router.post("/", response_model=OrderSchema, status_code=status.HTTP_201_CREATED)
async def create_order(
    payload: OrderCreate,
    db: AsyncIOMotorClient = Depends(get_database),
) -> OrderSchema:
    """[summary]
    View inserts item in the orders in list.

    [description]
    Endpoint to retrieve an specific item.
    """

    await orders.post(db, payload)


@router.get("/{id_}/")
async def read_note(
    id_: str,
    db: AsyncIOMotorClient = Depends(get_database),
) -> OrderSchema:
    """[summary]
    Get one item by ID.

    [description]
    Endpoint to retrieve an specific item.
    """
    return await orders.get(id_, db)


@router.get("/")
async def read_all_orders(
    status_order: Optional[str] = None,
    priority: Optional[int] = None,
    age: Optional[str] = None,
    value: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    db: AsyncIOMotorClient = Depends(get_database),
) -> List[OrderSchema]:
    """[summary]
    Get all item by ID.

    [description]
    Endpoint to retrieve an specific item.
    [optional]
    [ON CREATE] Filter order by status: ['to-do', 'doing', 'done']
    """
    filters = {
        "status": status_order,
        "priority": priority,
        "age": age,
        "value": value,
        "start_date": start_date,
        "end_date": end_date,
    }
    orders_list = await orders.get_all(db, filters)

    if not orders_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )

    return list(map(fix_item_id, orders_list))


@router.put("/{id_}/", response_model=OrderSchema)
async def update_item(
    id_: str,
    payload: OrderUpdate,
    db: AsyncIOMotorClient = Depends(get_database),
) -> OrderSchema:
    """[summary]
    Get alter item by ID.

    [description]
    Endpoint to retrieve an specific item.
    """
    return await orders.put(id_, payload, db)


@router.delete("/{id_}/")
async def delete_order(
    id_: str,
    db: AsyncIOMotorClient = Depends(get_database),
):
    """[summary]
    Get order item by ID.

    [description]
    Endpoint to retrieve an specific item.
    """
    await orders.delete(id_, db)


@router.delete("/")
async def remove_all(db: AsyncIOMotorClient = Depends(get_database)):
    """[summary]
    Get delete all orders

    [description]
    Endpoint to retrieve an specific item.
    """

    await orders.do_delete_many(db)
