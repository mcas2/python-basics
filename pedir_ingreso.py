# Pedir los datos de un estudiante y comprobar si puede entrar en un programa
# Nombre, edad, nota media y género (char)
# Si el nombre tiene menos de 3 letras -> bucle
# Si la nota es mayor que 5, la edad igual o mayor que 18 y el género F, ACEPTADA
# Si la nota es mayor que 5, la edad igual o mayor que 18 y el género M, ACEPTADO
# Si no se imprime no ACEPTADO

nombre = input("Nombre:\n")
while len(nombre) < 3:
    nombre = input("Introduce un nombre más largo:\n")

genero = input("Género:\n")
edad = int(input("Edad:\n"))
notaMedia = float(input("Nota media:\n"))

if notaMedia >= 5 and edad >= 18 and genero == "F":
    print("ACEPTADA")
elif notaMedia >= 5 and edad >= 18 and genero == "M":
    print("ACEPTADO")
else:
    print("NO ACEPTADO/A")
