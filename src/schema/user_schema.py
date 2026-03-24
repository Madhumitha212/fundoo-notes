from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name : str
    email : str
    password : str
    contact_no : Optional[str] = None
    is_active : Optional[bool] = False

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    contact_no: Optional[str] = None
    is_active: Optional[bool] = None

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool

    class Config:
        from_attributes = True