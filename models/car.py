from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Marca(Base):
    __tablename__ = 'marcas'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    modelos = relationship('Modelo', back_populates='marca')

class Modelo(Base):
    __tablename__ = 'modelos'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    marca_id = Column(Integer, ForeignKey('marcas.id'))
    marca = relationship('Marca', back_populates='modelos')
