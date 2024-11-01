# esta es una variable de lista []
frutas = ["manzana", "banano", "pera"]
frutas[0]="naranja"
print(frutas[0])

# esta es una variable de tipo tupla ()
paises = ("Mexico", "Guatemala", "Honduras", "Nicaragua")
# paises[0] = "El Salvador" 
print(paises[0])
print(type(paises))  

# esta es una variable de tipo diccionario {}
persona = {
    "id": "123456789-0",
    "nombre": "ana",
    "apellido": "pachecho",
    "edad": "19",
    "escolaridad": "primaria"
}

persona["nombre"] = "MARIA DE LOS ANGELES"
print("la persona con nombre {} tiene id {}: ".format(persona["nombre"], persona["id"]) )
print(type(persona))
