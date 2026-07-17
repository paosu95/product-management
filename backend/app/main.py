from fastapi import FastAPI

app = FastAPI(
    title="Nova Inventory API",
    description="API REST para la gestión de productos",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Nova Inventory API funcionando correctamente 🚀"
    }