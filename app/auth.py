from datetime import datetime, timedelta
from typing import Dict, Any
from fastapi import HTTPException
from passlib.context import CryptContext
from jose import jwt, JWTError
from .config import settings

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    """Verify a password against its hash."""
    return pwd_context.verify(password, hashed_password)

def create_access_token(data: Dict[str, Any], expires_delta: timedelta = timedelta(minutes=30)) -> str:
    """Create a JWT access token with the given data and expiration time."""
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt

def decode_token(token: str, secret_key: str = settings.JWT_SECRET_KEY) -> Dict[str, Any]:
    """Decode a JWT token and return its payload."""
    try:
        payload = jwt.decode(token, secret_key, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except JWTError as e:
        raise HTTPException(status_code=401, detail=f"Invalid token: {str(e)}")