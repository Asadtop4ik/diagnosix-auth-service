from pydantic import BaseModel, constr
from enum import Enum

class RoleEnum(str, Enum):
    patient = "patient"
    doctor = "doctor"
    admin = "admin"

class UserCreate(BaseModel):
    username: str
    password: str
    role: RoleEnum

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    role: RoleEnum

    class Config:
        from_attributes = True  # Updated for Pydantic V2