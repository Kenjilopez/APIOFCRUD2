from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class marca(Base):
    __tablename__ = 'marca'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), nullable=False)
    model = relationship('Model', back_populates= 'marca',cascade='all, delete-orphan')
    
class modelo(base):
    __tablename__ = 'modelos'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    marca.id = Column(Integer, ForeignKey('marca.id'))
    marca = relationship('marca', back_populates='model')
