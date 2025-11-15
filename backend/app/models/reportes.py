from sqlalchemy import Column, BigInteger, String, Text
from sqlalchemy.orm import relationship
from app.core.database import Base

class Reporte(Base):
    __tablename__ = "t_reportes"

    id_reporte = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String)
    descripcion = Column(Text)
    query_sql = Column(Text)
    tipo_exportacion = Column(String)

    filtros = relationship("FiltroReporte", back_populates="reporte")
