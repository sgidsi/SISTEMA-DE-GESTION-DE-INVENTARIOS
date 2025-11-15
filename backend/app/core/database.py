from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Cargar variables del .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está definido en el archivo .env")

# Convertir URL normal a versión async para SQLAlchemy
# Ejemplo:
# postgresql://user:pass@host:5432/db
# se convierte a:
# postgresql+asyncpg://user:pass@host:5432/db
ASYNC_DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

# Crear el engine asincrónico
engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=False,                 # Cambia a True solo para debug
    future=True,
    pool_size=5,
    max_overflow=10
)

# Crear el sessionmaker para generar sesiones de DB
async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base para los modelos
Base = declarative_base()

# Dependencia para obtener la sesión (para usar en los routers)
async def get_session():
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
