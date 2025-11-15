from sqlalchemy import Column, BigInteger, String, JSON, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Dashboard(Base):
    __tablename__ = "t_dashboard"

    id_dashboard = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String)
    usuario_asociado = Column(BigInteger, ForeignKey("t_usuarios.id_usuario"))
    configuracion_json = Column(JSON)
    visible_en_inicio = Column(Boolean, default=True)

    usuario = relationship("Usuario", back_populates="dashboards")
