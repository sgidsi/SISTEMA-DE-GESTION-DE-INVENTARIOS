from sqlalchemy import Column, BigInteger, String, Text
from app.core.database import Base

class Comprobante(Base):
    __tablename__ = "t_comprobante"

    id_comprobante = Column(BigInteger, primary_key=True, index=True)
    tipo = Column(String, nullable=False)
    plantilla = Column(Text)

    ventas = relationship("Venta", back_populates="comprobante")
