# APIOFCRUD2**

POST
http://localhost:5000/marcas

{
  "name": "Mazda",
  "modelos": ["Mazda3", "CX-5"]
}

PUT
http://localhost:5000/marcas/{id}
{
  "name": "Mazda Actualizado",
  "modelos": ["Mazda2", "CX-30"]
}

DELETE  
http://localhost:5000/marcas/{id}

GET 
http://127.0.0.1:5000/marcas/{id}
