from sqlalchemy import Column, BigInteger, String, Text
from sqlalchemy.orm import relationship
from app.core.database import Base

class Sucursal(Base):
    __tablename__ = "t_sucursal"

    id_sucursal = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String)
    direccion = Column(Text)
    telefono = Column(String)

    inventarios_sucursal = relationship("InventarioSucursal", back_populates="sucursal")
    usuarios = relationship("Usuario", back_populates="sucursal")
