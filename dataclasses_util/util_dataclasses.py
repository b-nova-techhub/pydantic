import dataclasses


@dataclasses.dataclass
class User:
    name: str
    age: int
    email: str
    is_active: bool
    is_admin: bool
    filepath: str
