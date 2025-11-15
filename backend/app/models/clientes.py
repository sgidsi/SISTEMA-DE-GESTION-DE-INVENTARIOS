from sqlalchemy import Column, BigInteger, String, Numeric, Text
from sqlalchemy.orm import relationship
from app.core.database import Base

class Cliente(Base):
    __tablename__ = "t_clientes"

    id_cliente = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    tipo = Column(String)
    correo = Column(String)
    telefono = Column(String)
    puntos_fidelidad = Column(Numeric, default=0)

    ventas = relationship("Venta", back_populates="cliente")
