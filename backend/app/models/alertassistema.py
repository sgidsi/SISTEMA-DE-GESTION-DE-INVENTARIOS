from sqlalchemy import Column, BigInteger, String, Text, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class AlertaSistema(Base):
    __tablename__ = "t_alertassistema"

    id_alerta = Column(BigInteger, primary_key=True, index=True)
    tipo_alerta = Column(String)
    descripcion = Column(Text)
    nivel_importancia = Column(String)
    fecha_generada = Column(DateTime, server_default=func.now())
    estado = Column(String)
    accion_recomendada = Column(Text)
