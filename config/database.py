from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Base de datos persistente en archivo local
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False},
    echo=True  # Muestra las consultas SQL en consola
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear las tablas al iniciar
from models.car import Base
Base.metadata.create_all(bind=engine)