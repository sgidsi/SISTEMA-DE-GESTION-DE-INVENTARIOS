from .auth_router import router as auth_router
from .usuarios_router import router as usuarios_router
from .productos_router import router as productos_router
from .categorias_router import router as categorias_router
from .proveedores_router import router as proveedores_router
from .clientes_router import router as clientes_router
from .ventas_router import router as ventas_router
from .compras_router import router as compras_router
from .inventarios_router import router as inventarios_router

__all__ = [
    "auth_router",
    "usuarios_router",
    "productos_router",
    "categorias_router",
    "proveedores_router",
    "clientes_router",
    "ventas_router",
    "compras_router",
    "inventarios_router",
]
