from sqlalchemy import Column, BigInteger, String, Text, JSON
from sqlalchemy.orm import relationship
from app.core.database import Base

class RubroSistema(Base):
    __tablename__ = "t_rubrossistema"

    id_rubro = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String)
    descripcion = Column(Text)
    modulos_activos = Column(JSON)
    plantilla_ui = Column(Text)

    plantillas = relationship("PlantillaComprobante", back_populates="rubro")
