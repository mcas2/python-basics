import random as r

def pintarCuadrado(longitud, simbolo):
    print(simbolo*longitud)
    for i in range(1, longitud-1):
        print(simbolo+" "*(longitud-2)+simbolo)
    print(simbolo*longitud)

def pintarLineaConEspacios(longitud, simbolo):
    lineaConEspacios = ""
    for j in range(longitud):
        if (j == 0 or j == longitud-1):
            lineaConEspacios += simbolo
        else:
            lineaConEspacios += " "
    return lineaConEspacios

def pintarCuadradoDobleBucle(longitud, simbolo):
    print(simbolo*longitud)
    lineaIntermedia = pintarLineaConEspacios(longitud, simbolo)
    for i in range(1, longitud-1):
        print(lineaIntermedia)
    print(simbolo*longitud)



numAleatorio = r.randint(169,223)
simboloAleatorio = chr(numAleatorio)
pintarCuadradoDobleBucle(5, simboloAleatorio)
