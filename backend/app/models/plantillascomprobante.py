from sqlalchemy import Column, BigInteger, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class PlantillaComprobante(Base):
    __tablename__ = "t_plantillascomprobante"

    id_plantilla = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String)
    tipo_comprobante = Column(String)
    html_css = Column(Text)
    empresa_asociada = Column(BigInteger, ForeignKey("t_empresa.id_empresa"))
    rubro_asociado = Column(BigInteger, ForeignKey("t_rubrossistema.id_rubro"))

    empresa = relationship("Empresa", back_populates="plantillas")
    rubro = relationship("RubroSistema", back_populates="plantillas")
