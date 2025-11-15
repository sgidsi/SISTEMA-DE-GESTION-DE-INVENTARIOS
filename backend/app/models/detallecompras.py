from sqlalchemy import Column, BigInteger, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.core.database import Base

class DetalleCompra(Base):
    __tablename__ = "t_detallecompras"

    id_detalle_compra = Column(BigInteger, primary_key=True, index=True)
    id_compra = Column(BigInteger, ForeignKey("t_compras.id_compra"))
    id_producto = Column(BigInteger, ForeignKey("t_productos.id_producto"))
    cantidad = Column(Numeric, nullable=False)
    precio_unitario = Column(Numeric, nullable=False)
    subtotal = Column(Numeric)

    compra = relationship("Compra", back_populates="detalles")
    producto = relationship("Producto", back_populates="detalles_compras")
