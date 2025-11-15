from sqlalchemy import Column, BigInteger, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base

class Usuario(Base):
    __tablename__ = "t_usuarios"

    id_usuario = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, nullable=False, unique=True)
    # 'contraseña' in DB -> map to python-friendly 'contrasena'
    contrasena = Column("contraseña", Text, nullable=False)
    id_rol = Column(BigInteger, ForeignKey("t_roles.id_rol"))
    id_sucursal = Column(BigInteger, ForeignKey("t_sucursal.id_sucursal"))
    activo = Column(Boolean, default=True)

    rol = relationship("Rol", back_populates="usuarios")
    sucursal = relationship("Sucursal", back_populates="usuarios")
    ventas = relationship("Venta", back_populates="usuario")
    dashboards = relationship("Dashboard", back_populates="usuario")
