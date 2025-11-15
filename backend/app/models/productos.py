from sqlalchemy import Column, BigInteger, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Producto(Base):
    __tablename__ = "t_productos"

    id_producto = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String, nullable=False, unique=True)
    descripcion = Column(Text)
    id_categoria = Column(BigInteger, ForeignKey("t_categoria.id_categoria"))
    codigo_barra = Column(String, unique=True)
    unidad_medida = Column(String)

    categoria = relationship("Categoria", back_populates="productos")
    inventario = relationship("Inventario", back_populates="producto", uselist=False, cascade="all, delete-orphan")
    inventarios_sucursal = relationship("InventarioSucursal", back_populates="producto")
    detalles_ventas = relationship("DetalleVenta", back_populates="producto")
    detalles_compras = relationship("DetalleCompra", back_populates="producto")
    sugerencias = relationship("SugerenciaCompra", back_populates="producto")
