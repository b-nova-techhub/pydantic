import json

from pydantic import BaseModel, EmailStr, FilePath


class User(BaseModel):
    name: str
    age: int
    email: EmailStr
    is_active: bool
    is_admin: bool
    filepath: FilePath


user_model_schema = User.model_json_schema()

# print(json.dumps(user_model_schema, indent=2))