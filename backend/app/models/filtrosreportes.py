from sqlalchemy import Column, BigInteger, ForeignKey, String, Text
from app.core.database import Base

class FiltroReporte(Base):
    __tablename__ = "t_filtrosreportes"

    id_filtro = Column(BigInteger, primary_key=True, index=True)
    id_reporte = Column(BigInteger, ForeignKey("t_reportes.id_reporte"))
    nombre_filtro = Column(String)
    tipo = Column(String)
    valor_predeterminado = Column(Text)

    reporte = relationship("Reporte", back_populates="filtros")
