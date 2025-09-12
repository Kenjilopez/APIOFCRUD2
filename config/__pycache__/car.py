from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Marca(Base):
    __tablename__ = 'marcas'
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String(250), nullable=False)
    modelos = relationship('Modelo', back_populates= 'marca',cascade='all, delete-orphan')
    
class Modelo(Base):
    __tablename__ = 'modelos'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    marca_id = Column(Integer, ForeignKey('marcas.id'))
    marca = relationship('Marca', back_populates='modelos')
