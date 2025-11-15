from sqlalchemy import Column, BigInteger, ForeignKey, Numeric, DateTime, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class SugerenciaCompra(Base):
    __tablename__ = "t_sugerenciascompra"

    id_sugerencia = Column(BigInteger, primary_key=True, index=True)
    id_producto = Column(BigInteger, ForeignKey("t_productos.id_producto"))
    cantidad_recomendada = Column(Numeric)
    sucursal = Column(BigInteger, ForeignKey("t_sucursal.id_sucursal"))
    fecha_generada = Column(DateTime, server_default=func.now())
    estado = Column(String)

    producto = relationship("Producto", back_populates="sugerencias")
    sucursal_rel = relationship("Sucursal")
