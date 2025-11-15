from sqlalchemy import Column, BigInteger, ForeignKey, DateTime, Numeric
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Venta(Base):
    __tablename__ = "t_ventas"

    id_venta = Column(BigInteger, primary_key=True, index=True)
    id_cliente = Column(BigInteger, ForeignKey("t_clientes.id_cliente"))
    fecha = Column(DateTime, server_default=func.now(), nullable=False)
    total = Column(Numeric, nullable=False)
    id_comprobante = Column(BigInteger, ForeignKey("t_comprobante.id_comprobante"))
    id_usuario = Column(BigInteger, ForeignKey("t_usuarios.id_usuario"))

    cliente = relationship("Cliente", back_populates="ventas")
    comprobante = relationship("Comprobante", back_populates="ventas")
    usuario = relationship("Usuario", back_populates="ventas")
    detalles = relationship("DetalleVenta", back_populates="venta", cascade="all, delete-orphan")
