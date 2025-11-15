from sqlalchemy import Column, BigInteger, ForeignKey, Numeric, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Inventario(Base):
    __tablename__ = "t_inventario"

    id_inventario = Column(BigInteger, primary_key=True, index=True)
    id_producto = Column(BigInteger, ForeignKey("t_productos.id_producto"))
    stock_actual = Column(Numeric, default=0)
    stock_minimo = Column(Numeric, default=0)
    stock_maximo = Column(Numeric)
    fecha_actualizacion = Column(DateTime, server_default=func.now())

    producto = relationship("Producto", back_populates="inventario")
