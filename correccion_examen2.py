"""permita introducir 5 numeros
guardalos y recorrela llamando a una funcion
que devuelva sus raices cuadradas
crea una función que diga si son enteros o decimales
imprime"""
import math

def raizCuadrada(numero):
    return math.sqrt(numero)

def esEntero(numero):
    cifras = str(numero)
    if cifras[len(cifras)-1] == "0" and cifras[len(cifras)-2] == ".":
        return True
    return False

numeros = []
for i in range(5):
    numeros.append(int(input(f"Introduce el número {i+1}: ")))

for i in range(len(numeros)):
    numero = numeros[i]
    raiz = raizCuadrada(numero)
    entero = esEntero(raiz)
    if entero:
        print(f"La raiz de {numero} es {raiz} y es entera.")
    else:
        print(f"La raiz de {numero} es {raiz} y es decimal.")