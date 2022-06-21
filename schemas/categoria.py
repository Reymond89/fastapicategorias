from unicodedata import name
from pydantic import BaseModel
from typing import Optional

class Category(BaseModel):
    id: Optional[str]
    ref: int
    name: str
