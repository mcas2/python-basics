"""Crear un programa en el que puedas hacer la quiniela.
 Tendremos dos arrays de equipos,uno con los locales y otro con
 sus correspondientes visitantes. Al usuario se le mostrará el
 enfrentamiento y tendrá que marcar 1 si cree que ganará el local,
  2 si el visitante o X en caso de empate.
  El programa mostrará la elección final."""
import random

def validarEntrada(entrada):
    while entrada.upper() not in ["1", "2", "X"]:
        entrada = input("Introduce un valor correcto: 1, 2 o X => ")
    return entrada

def pintarLinea():
    print("=============================================")

def apuestasUsuario():
    apuestas = []
    for i in range(len(locales)):
        apuesta = validarEntrada(input(f"{locales[i]} - {visitantes[i]} => "))
        apuestas.append(apuesta)
    return apuestas

def imprimirResultados(resultados):
    for i in range(len(resultados)):
        pintarLinea()
        print(f"{locales[i]} - {visitantes[i]} : {resultados[i]}")

def comprobarResultados(resultados, apuestas):
    cont = 0
    for i in range(len(resultados)):
        if resultados[i] == apuestas[i]:
            cont += 1
    return cont


locales = ["FC Barcelona","Real Madrid","Atlético de Madrid","Villarreal",
           "Athletic Club de Bilbao","Osasuna","Girona","Mallorca",
           "Real Betis","Real Sociedad"]
visitantes = ["Celta de Vigo","Sevilla","Rayo Vallecano","CD Leganés","Getafe",
"Deportivo Alavés","UD Las Palmas","Valencia","RCD Espanyol","Real Valladolid"]
posiblesResultados = ["1","2","X"]
resultados = []

for i in range(len(locales)):
    resultados.append(posiblesResultados[random.randint(0,2)])

apuestas = apuestasUsuario()
imprimirResultados(resultados)
print("**********************")
print("**********************")
print("**********************")
imprimirResultados(apuestas)

victorias = comprobarResultados(resultados, apuestas)
print(f"Has acertado {victorias} veces y fallado {len(resultados)-victorias}")