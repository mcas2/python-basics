"""Multiplicación de dos listas
Escribe una función llamada 'multiplicarListas'
que reciba dos listas de números de igual longitud
y devuelva una nueva lista donde cada elemento es el
resultado de multiplicar los elementos correspondientes
de ambas listas. Utiliza un bucle 'for'.
Si las listas tienen diferente longitud,
la función debe devolver un mensaje indicando que las listas
no son del mismo tamaño. La función debe devolver la lista
con los productos de los elementos correspondientes de ambas listas.
"""

def multiplicarListas(listaUno, listaDos):
    if (len(listaUno) != len(listaDos)):
        return "No son del mismo tamaño"
    listaFinal = []
    for i in range(len(listaUno)):
        listaFinal.append(listaUno[i]*listaDos[i])

    return listaFinal

precios = [2,3,5]
cantidades = [1,3,2]
resultado = multiplicarListas(precios, cantidades)
print(resultado)

