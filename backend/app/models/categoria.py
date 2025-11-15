from sqlalchemy import Column, BigInteger, String, Text
from sqlalchemy.orm import relationship
from app.core.database import Base

class Categoria(Base):
    __tablename__ = "t_categoria"

    id_categoria = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(Text)

    productos = relationship("Producto", back_populates="categoria", cascade="all, delete-orphan")
