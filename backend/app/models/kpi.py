from sqlalchemy import Column, BigInteger, String, Text, Numeric
from app.core.database import Base

class KPI(Base):
    __tablename__ = "t_kpi"

    id_kpi = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String)
    descripcion = Column(Text)
    formula_sql = Column(Text)
    unidad_medida = Column(String)
    umbral_alerta = Column(Numeric)
