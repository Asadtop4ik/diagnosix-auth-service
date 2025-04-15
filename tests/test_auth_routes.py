import pytest
from fastapi import status
from app.auth import create_access_token
from app.models import RoleEnum

@pytest.mark.asyncio
async def test_register_user(client, test_db):
    response = client.post(
        "/auth/register",
        json={"username": "newuser", "password": "newpass", "role": RoleEnum.patient.value}  # .value qo'shildi
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["username"] == "newuser"
    assert data["role"] == "patient"
    assert "id" in data

@pytest.mark.asyncio
async def test_register_user_already_exists(client, test_user):
    response = client.post(
        "/auth/register",
        json={"username": "testuser", "password": "testpass", "role": RoleEnum.patient.value}  # .value qo'shildi
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == "Username already exists"

@pytest.mark.asyncio
async def test_login_success(client, test_user):
    response = client.post(
        "/auth/login",
        json={"username": "testuser", "password": "testpass"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

@pytest.mark.asyncio
async def test_login_invalid_credentials(client, test_user):
    response = client.post(
        "/auth/login",
        json={"username": "testuser", "password": "wrongpass"}
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json()["detail"] == "Invalid credentials"

@pytest.mark.asyncio
async def test_get_me(client, test_user):
    token = create_access_token({"sub": "testuser", "role": "patient"})
    response = client.get(
        "/auth/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["username"] == "testuser"
    assert data["role"] == "patient"