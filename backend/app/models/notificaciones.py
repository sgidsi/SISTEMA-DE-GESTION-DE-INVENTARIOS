from sqlalchemy import Column, BigInteger, String, Text, DateTime
from app.core.database import Base

class Notificacion(Base):
    __tablename__ = "t_notificaciones"

    id_notificacion = Column(BigInteger, primary_key=True, index=True)
    tipo = Column(String)
    destinatario = Column(Text)
    mensaje = Column(Text)
    estado = Column(String)
    fecha_envio = Column(DateTime)
    modulo_asociado = Column(String)
