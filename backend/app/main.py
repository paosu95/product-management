from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.database.database import Base, engine
from app.models import Product, History
from app.routers.products import router as product_router
from app.routers.history import router as history_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Nova Inventory API",
    description="API REST para la gestión de productos",
    version="1.0.0",
)

# ---------------- CORS ----------------
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --------------------------------------

app.include_router(product_router)
app.include_router(history_router)


@app.get("/")
def root():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {
        "message": "Nova Inventory API funcionando correctamente 🚀",
        "database": "Conectada correctamente",
    }