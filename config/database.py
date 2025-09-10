from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Base de datos en memoria (los datos se pierden al cerrar la aplicación)
DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False},
    echo=True  # Muestra las consultas SQL en consola
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear las tablas al iniciar
from car import Base
Base.metadata.create_all(bind=engine)