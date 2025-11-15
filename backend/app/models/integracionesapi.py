from sqlalchemy import Column, BigInteger, String, Text, Boolean, DateTime
from app.core.database import Base

class IntegracionAPI(Base):
    __tablename__ = "t_integracionesapi"

    id_integracion = Column(BigInteger, primary_key=True, index=True)
    nombre_servicio = Column(String)
    tipo = Column(String)
    url_base = Column(Text)
    api_key = Column(Text)
    estado = Column(Boolean, default=True)
    ultimo_log = Column(DateTime)
