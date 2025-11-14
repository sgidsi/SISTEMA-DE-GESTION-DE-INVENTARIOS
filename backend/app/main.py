from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import productos

app = FastAPI(title="Sistema de Inventario Universal - Backend")

origins = ["http://localhost:5173"]  # frontend local

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(productos.router, prefix="/productos", tags=["Productos"])

@app.get("/")
def read_root():
    return {"status": "success", "data": [], "message": "API corriendo"}
