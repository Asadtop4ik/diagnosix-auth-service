from sqlalchemy import Column, Integer, String, Enum
from app.database import Base
import enum

# Define RoleEnum for SQLAlchemy (mirrors the RoleEnum in schemas.py)
class RoleEnum(str, enum.Enum):
    patient = "patient"
    doctor = "doctor"
    admin = "admin"

# SQLAlchemy model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)  # Renamed for clarity
    role = Column(Enum(RoleEnum), nullable=False)  # Use SQLAlchemy Enum