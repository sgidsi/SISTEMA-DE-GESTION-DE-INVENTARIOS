from sqlalchemy import Column, BigInteger, String, JSON
from sqlalchemy.orm import relationship
from app.core.database import Base

class Rol(Base):
    __tablename__ = "t_roles"

    id_rol = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    permisos = Column(JSON)

    usuarios = relationship("Usuario", back_populates="rol")
