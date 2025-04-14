from fastapi import FastAPI
from .routes import auth_routes
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Diagnosix Auth Service")

app.include_router(auth_routes.router)
