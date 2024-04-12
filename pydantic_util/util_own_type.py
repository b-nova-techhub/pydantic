from typing import Annotated
from annotated_types import Gt
from pydantic import BaseModel, EmailStr, FilePath, TypeAdapter

positivInt = Annotated[int, Gt(0)]

ta = TypeAdapter(positivInt)

class User(BaseModel):
    name: str
    age: int
    email: EmailStr
    is_active: bool = True
    is_admin: bool = False
    filepath: FilePath
    bought: positivInt


