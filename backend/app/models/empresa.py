from sqlalchemy import Column, BigInteger, String, Text
from app.core.database import Base

class Empresa(Base):
    __tablename__ = "t_empresa"

    id_empresa = Column(BigInteger, primary_key=True, index=True)
    razon_social = Column(String)
    ruc = Column(String, unique=True)
    direccion = Column(Text)
    telefono = Column(String)
    correo = Column(String)
    api_key_sunat = Column(Text)
    modo_facturacion = Column(String)

    plantillas = relationship("PlantillaComprobante", back_populates="empresa")
