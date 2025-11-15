from sqlalchemy import Column, BigInteger, String, Text
from sqlalchemy.orm import relationship
from app.core.database import Base

class Proveedor(Base):
    __tablename__ = "t_proveedores"

    id_proveedor = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    ruc = Column(String, unique=True)
    telefono = Column(String)
    direccion = Column(Text)
    email = Column(String)

    compras = relationship("Compra", back_populates="proveedor")
