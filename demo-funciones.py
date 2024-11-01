pelicula = {
    "id": 123,
    "nombre": "Wild Robot"
}

lista=[]

lista.insert(pelicula)
def sumar(valor1, valor2, valor3, valor4, pelicula, lista):
    print("El nombre de la pelicula es : " + pelicula["nombre"])
    resultado=valor1+valor2
    return resultado
    

v1=int(input("cual es el valor 1:\n"))
v2=int(input("cual es el valor 2:\n"))
#print(sumar(valor1=v1, valor2=v2)
print("El resultado es: \n", sumar(v1, v2, 0, 0, pelicula, lista))