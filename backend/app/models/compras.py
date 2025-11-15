from sqlalchemy import Column, BigInteger, ForeignKey, DateTime, Numeric, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Compra(Base):
    __tablename__ = "t_compras"

    id_compra = Column(BigInteger, primary_key=True, index=True)
    id_proveedor = Column(BigInteger, ForeignKey("t_proveedores.id_proveedor"))
    fecha = Column(DateTime, server_default=func.now(), nullable=False)
    total = Column(Numeric, nullable=False)
    estado = Column(String, nullable=False, server_default="pendiente")

    proveedor = relationship("Proveedor", back_populates="compras")
    detalles = relationship("DetalleCompra", back_populates="compra", cascade="all, delete-orphan")
