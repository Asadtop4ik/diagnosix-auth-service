import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.main import app
from app.routes.auth_routes import get_db
from app.models import User, RoleEnum

# Test uchun SQLite bazasini sozlash
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# TestClient va DB sessionni sozlash
@pytest.fixture(scope="function")
def client():
    # Har bir testdan oldin bazani yaratish
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


@pytest.fixture(scope="function")
def test_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def test_user(test_db):
    # Test foydalanuvchi yaratish
    from app.auth import hash_password
    user = User(
        username="testuser",
        hashed_password=hash_password("testpass"),
        role=RoleEnum.patient
    )
    test_db.add(user)
    test_db.commit()
    test_db.refresh(user)
    return user