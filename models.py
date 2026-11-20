from sqlalchemy import Column, Integer, String
from database import Base


class Servicio(Base):
    # Nombre de la tabla
    __tablename__ = "servicios"

    # Columnas de la tabla
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String(200), nullable=False)