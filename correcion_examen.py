"""palabras aleatorias
primera letra mayúscula
el resto minúscula
c-v-c-v
longitud usuario"""
import random as r

def generarPalabra(longitud):
    palabra = ""
    for i in range(longitud):
        if (i%2 == 0):
            palabra += consonantes[r.randint(0, len(consonantes)-1)]
        else:
            palabra += vocales[r.randint(0, len(vocales)-1)]
    return palabra.capitalize()

consonantes = ["b","c","d","f","g","h","j","k","l","m","n","ñ",
    "p","q","r","s","t","v","w","x","y","z"]
vocales = ["a", "e", "i", "o", "u"]

longitudPalabra = int(input("Dame la longitud de la palabra: "))
print(f"Tu palabra es {generarPalabra(longitudPalabra)}")
