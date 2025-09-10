from flask import Flask
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.car_controllers import marca_bp
from config.database import engine
from models.car import Base

# Crear tablas si no existen
def create_tables():
    Base.metadata.create_all(bind=engine)

app = Flask(__name__)
app.register_blueprint(marca_bp)

if __name__ == '__main__':
    create_tables()
    app.run(debug=True, host='0.0.0.0')
