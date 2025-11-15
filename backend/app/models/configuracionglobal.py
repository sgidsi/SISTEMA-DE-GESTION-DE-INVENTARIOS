from sqlalchemy import Column, BigInteger, String, Numeric
from app.core.database import Base

class ConfiguracionGlobal(Base):
    __tablename__ = "t_configuracionglobal"

    id_configuracion_global = Column(BigInteger, primary_key=True, index=True)
    moneda_predeterminada = Column(String)
    simbolo_moneda = Column(String)
    idioma = Column(String)
    zona_horaria = Column(String)
    formato_fecha = Column(String)
    formato_hora = Column(String)
    porcentaje_iva = Column(Numeric)
    modo_facturacion = Column(String)
