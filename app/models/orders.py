from pydantic import BaseModel, Field, validator
from typing import Optional
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

    @validator("due_at")
    def validate_due_at(cls, v):
        try:
            datetime.fromisoformat(v)
            return v
        except:
            raise ValueError("Due date must to be in ISO format")


class OrderBaseSchema(Timestamp):
    status: OperationStatusEnum = OperationStatusEnum.TODO
    priority: PriorityEnum = PriorityEnum.LOW
    age: Optional[str] = Field(min_length=2, max_length=10)
    value: Optional[str] = Field(min_length=2, max_length=10)


class OrderCreate(OrderBaseSchema):
    created_at: str = datetime.utcnow().isoformat()


class OrderUpdate(OrderBaseSchema):
    status: Optional[OperationStatusEnum]
    priority: Optional[PriorityEnum]
    age: Optional[str] = Field(min_length=2, max_length=3)
    value: Optional[str] = Field(min_length=2, max_length=10)


class OrderInDb(OrderBaseSchema):
    id: str = Field(alias="_id")

    @validator("id", pre=True)
    def convert_object_id_to_str(cls, v):
        return str(v)

    class Config:
        orm_mode = True


class OrderSchema(OrderInDb):
    pass


def fix_item_id(item):
    try:
        item["_id"] = str(item["_id"])
    except KeyError:
        raise ValueError(f"No `_id` found! Unable to fix item ID for item: {item}")
    else:
        return item
