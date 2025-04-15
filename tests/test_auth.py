import pytest
from datetime import timedelta
from app.auth import hash_password, verify_password, create_access_token, decode_token
from app.config import settings

def test_hash_and_verify_password():
    password = "testpass123"
    hashed = hash_password(password)
    assert verify_password(password, hashed) is True
    assert verify_password("wrongpass", hashed) is False

def test_create_and_decode_token():
    data = {"sub": "testuser", "role": "patient"}
    token = create_access_token(data, expires_delta=timedelta(minutes=1))
    decoded = decode_token(token)
    assert decoded["sub"] == "testuser"
    assert decoded["role"] == "patient"
    assert "exp" in decoded

def test_decode_invalid_token():
    with pytest.raises(Exception) as exc_info:
        decode_token("invalid.token.here")
    assert "Invalid token" in str(exc_info.value)