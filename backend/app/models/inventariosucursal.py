from sqlalchemy import Column, BigInteger, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.core.database import Base

class InventarioSucursal(Base):
    __tablename__ = "t_inventariosucursal"

    id_inventario_sucursal = Column(BigInteger, primary_key=True, index=True)
    id_sucursal = Column(BigInteger, ForeignKey("t_sucursal.id_sucursal"))
    id_producto = Column(BigInteger, ForeignKey("t_productos.id_producto"))
    stock = Column(Numeric, default=0)

    sucursal = relationship("Sucursal", back_populates="inventarios_sucursal")
    producto = relationship("Producto", back_populates="inventarios_sucursal")
