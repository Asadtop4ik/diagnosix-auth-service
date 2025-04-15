from datetime import datetime, timedelta, UTC  # UTC qo'shildi
from typing import Dict, Any
from fastapi import HTTPException
from passlib.context import CryptContext
from jose import jwt, JWTError
from .config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:

    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:

    return pwd_context.verify(password, hashed_password)

def create_access_token(data: Dict[str, Any], expires_delta: timedelta = timedelta(minutes=30)) -> str:

    to_encode = data.copy()
    expire = datetime.now(UTC) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt

def decode_token(token: str, secret_key: str = settings.JWT_SECRET_KEY) -> Dict[str, Any]:

    try:
        payload = jwt.decode(token, secret_key, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except JWTError as e:
        raise HTTPException(status_code=401, detail=f"Invalid token: {str(e)}")