from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import (
    auth_router,
    usuarios_router,
    productos_router,
    categorias_router,
    proveedores_router,
    clientes_router,
    ventas_router,
    compras_router,
    inventarios_router
)

app = FastAPI(title="Sistema de Gestión de Inventarios")

# CORS para permitir frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Puedes restringir esto más adelante
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar routers
app.include_router(auth_router.router, prefix="/auth", tags=["Auth"])
app.include_router(usuarios_router.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(productos_router.router, prefix="/productos", tags=["Productos"])
app.include_router(categorias_router.router, prefix="/categorias", tags=["Categorias"])
app.include_router(proveedores_router.router, prefix="/proveedores", tags=["Proveedores"])
app.include_router(clientes_router.router, prefix="/clientes", tags=["Clientes"])
app.include_router(ventas_router.router, prefix="/ventas", tags=["Ventas"])
app.include_router(compras_router.router, prefix="/compras", tags=["Compras"])
app.include_router(inventarios_router.router, prefix="/inventarios", tags=["Inventarios"])
