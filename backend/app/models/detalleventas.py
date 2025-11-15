from sqlalchemy import Column, BigInteger, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.core.database import Base

class DetalleVenta(Base):
    __tablename__ = "t_detalleventas"

    id_detalle_venta = Column(BigInteger, primary_key=True, index=True)
    id_venta = Column(BigInteger, ForeignKey("t_ventas.id_venta"))
    id_producto = Column(BigInteger, ForeignKey("t_productos.id_producto"))
    cantidad = Column(Numeric, nullable=False)
    precio_unitario = Column(Numeric, nullable=False)
    descuento = Column(Numeric, default=0)
    subtotal = Column(Numeric)

    venta = relationship("Venta", back_populates="detalles")
    producto = relationship("Producto", back_populates="detalles_ventas")
