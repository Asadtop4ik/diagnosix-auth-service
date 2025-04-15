from pydantic import BaseModel, ConfigDict
from enum import Enum

class RoleEnum(str, Enum):
    patient = "patient"
    doctor = "doctor"
    admin = "admin"

class UserCreate(BaseModel):
    username: str
    password: str
    role: RoleEnum

    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    username: str
    password: str

    model_config = ConfigDict(from_attributes=True)

class UserResponse(BaseModel):
    id: int
    username: str
    role: RoleEnum

    model_config = ConfigDict(from_attributes=True)