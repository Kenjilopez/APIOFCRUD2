from config.database import SessionLocal
from car import Marca,Modelo
from sqlalchemy.orm import joinedload

def get_all_marca():
    session = SessionLocal()
    marcas = session.query(marca).options(joinedload(marca.model)).all()
    result = []
    for marca in marcas:
        result.append({
            'id': marca.id,
            'name': marca.name,
            'modelo': [{'id': modelo.id, 'title': modelo.title} for modelo in marca.modelos]
        })
    session.close()
    return result

def get_car_by_id(marca_id):
    session = SessionLocal()
    marca = session.query(Marca).options(joinedload(Marca.modelos)).filter(Marca.id == marca_id).first()
    if marca:
        result = {
            'id': marca.id,
            'name': marca.name,
            'modelo':[{'id': modelo.id, 'title': modelo.title} for modelo in marca.modelos]
        }
    else:
        result = None
    session.close()
    return result

def create_marca(data):
    session = SessionLocal()
    marca = Marca(name=data['name'])
    session.add(marca)
    session.commit()

    for modelo_title in data.get('modelos', []):
        modelo = Modelo(title=modelo_title, marca_id=marca.id)
        session.add(modelo)
    session.commit()
    result = {
        'id': marca.id,
        'name': marca.name,
        'modelos': [modelo.title for modelo in marca.modelos]
    }
    session.close()
    return result

def update_marca(marca_id, data):
    session = SessionLocal()
    marca = session.query(Marca).filter(Marca.id == marca_id).first()
    if not marca:
        session.close()
        return None
    marca.name = data.get('name', marca.name)
    if 'modelos' in data:
        session.query(Modelo).filter(Modelo.marca_id == marca_id).delete()
        for modelo_title in data['modelos']:
            modelo = Modelo(title=modelo_title, marca_id=marca.id)
            session.add(modelo)
    session.commit()
    result = {
        'id': marca.id,
        'name': marca.name,
        'modelos': [modelo.title for modelo in marca.modelos]
    }
    session.close()
    return result

def delete_marca(marca_id):
    session = SessionLocal()
    marca = session.query(Marca).filter(Marca.id == marca_id).first()
    if not marca:
        session.close()
        return False
    session.delete(marca)
    session.commit()
    session.close()
    return True