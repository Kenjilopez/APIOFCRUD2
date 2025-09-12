# APIOFCRUD2**
Para correr la Api usar App.py

Para correr las instrucciones CRUD usar Postman


POST ---Crear---
http://localhost:5000/marcas
{
  "name": "Mazda",
  "modelos": ["Mazda3", "CX-5"]
}

PUT ----Actualizar----
http://localhost:5000/marcas/{id}
{
  "name": "Mazda Actualizado",
  "modelos": ["Mazda2", "CX-30"]
}

DELETE  ----Eliminar---
http://localhost:5000/marcas/{id}

GET  ----Obtener todos los datos----
http://127.0.0.1:5000/marcas/{id}
