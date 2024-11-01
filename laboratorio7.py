

# if  # elif # else

edadEstudiante = int(input("Ingrese su edad: "))

# si el estudiante es mayor o igual que 18
if edadEstudiante >= 18:
    print("El estudiante ya debe pagar mensualidad")
## si el estudiante es mayor o igual que 10 y menor a 18
elif edadEstudiante >= 10 and edadEstudiante < 18:
    print("El estudiante tiene media beca")
elif edadEstudiante >= 5 and edadEstudiante < 10:
    print("lo que sea")
# de lo contrario hacer esto
else:
    print("El estudiante puede ser becado")