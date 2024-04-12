from pydantic import EmailStr
from pydantic.dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
    email: EmailStr
    is_active: bool
    is_admin: bool
    filepath: str
