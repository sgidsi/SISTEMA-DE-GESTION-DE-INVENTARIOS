from sqlalchemy import Column, String, Text
from app.core.database import Base

class ParametroSistema(Base):
    __tablename__ = "t_parametrossistema"

    nombre_parametro = Column(String, primary_key=True, index=True)
    valor = Column(Text)
    descripcion = Column(Text)
    modulo = Column(String)
