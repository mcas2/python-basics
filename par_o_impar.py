#Programa que me dice si un número es par o impar
#Función que devuelve un booleano (True) si el numero que le llega
#como argumento es par
# El usuario introduce un numero, se llama a la funcion, se comprueba el
#booleano y se imprime el resultado

def esPar(numero):
    return numero % 2 == 0

numeroUsuario = int(input("Introduce un número\n"))

if esPar(numeroUsuario):
    print("Es par")
else:
    print("No es par")