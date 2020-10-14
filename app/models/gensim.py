from pydantic import BaseModel
from typing import Dict

class DocumentSchema(BaseModel):
    document: str

def fix_item_id(item):
    if item.get("_id", False):
        item["_id"] = str(item["_id"])
        return item
    else:
        raise ValueError(
            f"No `_id` found! Unable to fix item ID for item: {item}")
