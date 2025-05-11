from pydantic import BaseModel
from typing import List

class TagSchema(BaseModel):
    id: int
    name: str

class UserSchema(BaseModel):
    id: int
    subject: str
    email: str | None
    phone: int | None
    tags: List[TagSchema]
