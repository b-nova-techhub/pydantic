from pydantic import BaseModel, EmailStr, FilePath


class User(BaseModel):
    name: str
    age: int
    email: EmailStr
    is_active: bool
    is_admin: bool
    filepath: FilePath
