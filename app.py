from flask import Flask
from controllers.car_controllers import marca_bp

app = Flask(__name__)
app.register_blueprint(marca_bp)

from config.database import SessionLocal
from models.car import Marca, Modelo

def insertar_datos_iniciales():
    session = SessionLocal()
    if session.query(Marca).count() == 0:
        datos = [
            {"name": "Toyota", "modelos": ["Corolla", "Camry"]},
            {"name": "Honda", "modelos": ["Civic", "Accord"]},
            {"name": "Ford", "modelos": ["Focus", "Fiesta"]},
            {"name": "Chevrolet", "modelos": ["Aveo", "Onix"]},
            {"name": "Nissan", "modelos": ["Sentra", "Versa"]},
            {"name": "Mazda", "modelos": ["Mazda3", "CX-5"]},
            {"name": "Volkswagen", "modelos": ["Jetta", "Golf"]},
            {"name": "Hyundai", "modelos": ["Elantra", "Tucson"]},
            {"name": "Kia", "modelos": ["Rio", "Sportage"]},
            {"name": "Renault", "modelos": ["Logan", "Sandero"]}
        ]
        for marca_data in datos:
            marca = Marca(name=marca_data["name"])
            session.add(marca)
            session.commit()
            for modelo_nombre in marca_data["modelos"]:
                modelo = Modelo(title=modelo_nombre, marca_id=marca.id)
                session.add(modelo)
            session.commit()
    session.close()

if __name__ == "__main__":
    insertar_datos_iniciales()
    app.run(debug=True, host="0.0.0.0", port=5000)
