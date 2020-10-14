from typing import List, Optional
from fastapi import APIRouter, HTTPException, Depends, status

from app.payloads import notes
from app.models.notes import NoteCreate, NoteSchema, fix_item_id, NoteUpdate
from app.models.users import UserSchema
from ....db.mongodb import AsyncIOMotorClient, get_database
from .utils import get_current_user


router = APIRouter()


@router.post("/", response_model=NoteSchema, status_code=status.HTTP_201_CREATED)
async def create_note(
    payload: NoteCreate,
    db: AsyncIOMotorClient = Depends(get_database), 
    current_user: UserSchema = Depends(get_current_user)
) -> NoteSchema:
    """[summary]
    View inserts item in the note list.

    [description]
    Endpoint to retrieve an specific item.
    """
    await notes.post(db, payload, current_user)


@router.get("/{id_}/")
async def read_note(
    id_: str, 
    db:AsyncIOMotorClient = Depends(get_database), 
    current_user: UserSchema = Depends(get_current_user)
) -> NoteSchema:
    """[summary]
    Get one item by ID.

    [description]
    Endpoint to retrieve an specific item.
    """    
    return await notes.get(id_, db, current_user)


@router.get("/")
async def read_all_notes(
    status_note: Optional[str] = None,
    priority: Optional[int] = None,
    tags: Optional[List[str]] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    db: AsyncIOMotorClient = Depends(get_database),
    current_user: UserSchema = Depends(get_current_user)
)-> List[NoteSchema]:
    """[summary]
    Get all item by ID.

    [description]
    Endpoint to retrieve an specific item.
    [optional]
    Filter note by status: ['to-do', 'doing', 'done']
    """  
    filters = {
        'status': status_note,
        'priority': priority,
        'tags': tags,
        'start_date': start_date,
        'end_date': end_date
    }
    notes_list = await notes.get_all(db, filters, current_user)

    if not notes_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")    

    return list(map(fix_item_id, notes_list))


@router.put("/{id_}/", response_model=NoteSchema)
async def update_item(
    id_: str, 
    payload: NoteUpdate, 
    db:AsyncIOMotorClient = Depends(get_database),
    current_user: UserSchema = Depends(get_current_user)
) -> NoteSchema:
    """[summary]
    Get alter item by ID.

    [description]
    Endpoint to retrieve an specific item.
    """
    return await notes.put(id_, payload, db, current_user)


@router.delete("/{id_}/")
async def delete_note(
    id_: str, 
    db:AsyncIOMotorClient = Depends(get_database),
    current_user: UserSchema = Depends(get_current_user)
):
    """[summary]
    Get delete item by ID.

    [description]
    Endpoint to retrieve an specific item.
    """  
    await notes.delete(id_, db, current_user)


@router.delete("/")
async def remove_all(db: AsyncIOMotorClient = Depends(get_database)):
    """[summary]
    Get delete all notes

    [description]
    Endpoint to retrieve an specific item.
    """

    await notes.do_delete_many(db)
