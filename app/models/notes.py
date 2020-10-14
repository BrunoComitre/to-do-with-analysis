from pydantic import BaseModel, Field, validator, ValidationError
from typing import Optional, List
from enum import Enum, IntEnum
from datetime import datetime, timedelta

class OperationStatusEnum(str, Enum):
    TODO = "todo"
    DOING = "doing"
    DONE = "done"

class PriorityEnum(IntEnum):
    LOW = 30
    MEDIUM = 20
    HIGH = 10

class Timestamp(BaseModel):
    created_at: Optional[str]
    modified_at: Optional[str]
    due_at: str = (datetime.utcnow() + timedelta(days=7)).isoformat()

    @validator('due_at')
    def validate_due_at(cls, v):
        try:
            datetime.fromisoformat(v)
            return v
        except:
            raise ValueError('Due date must to be in ISO format')

class NoteBaseSchema(Timestamp):
    status: OperationStatusEnum = OperationStatusEnum.TODO
    priority: PriorityEnum = PriorityEnum.LOW
    description: str = Field(min_length=3, max_length=100)
    tag: List[str] = Field(min_length=3, max_length=15)
    owner: Optional[str]
    participants: Optional[List[str]]

class NoteCreate(NoteBaseSchema):
    created_at: str = datetime.utcnow().isoformat()
    
class NoteUpdate(NoteBaseSchema):
    status: Optional[OperationStatusEnum]
    priority: Optional[PriorityEnum]
    description: Optional[str] = Field(min_length=3, max_length=100)
    tag: Optional[List[str]] = Field(min_length=3, max_length=15)
    participants: Optional[List[str]]

class NoteInDb(NoteBaseSchema):
    id: str = Field(alias="_id")


    @validator('id', pre=True)
    def convert_object_id_to_str(cls, v):
        return str(v)
    
    class Config:
        orm_mode = True

class NoteSchema(NoteInDb):
    pass

def fix_item_id(item):
    # if item.get("_id", False):
    #     item["_id"] = str(item["_id"])
    #     return item
    # else:
    #     raise ValueError(
    #         f"No `_id` found! Unable to fix item ID for item: {item}")
    
    try:
        item['_id'] = str(item['_id'])
    except KeyError:
        raise ValueError(
            f"No `_id` found! Unable to fix item ID for item: {item}")
    else:
        return item
