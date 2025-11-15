from sqlalchemy import Column, BigInteger, String, DateTime, JSON
from sqlalchemy.sql import func
from app.core.database import Base

class LogIA(Base):
    __tablename__ = "t_logia"

    id_log = Column(BigInteger, primary_key=True, index=True)
    tipo_analisis = Column(String)
    resultado_json = Column(JSON)
    fecha_generado = Column(DateTime, server_default=func.now())
