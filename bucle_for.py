# Pida una entrada de texto al usuario y
# que en un bucle for se imprima cada una de sus letras
# nombre = input("Introduce tu nombre \n")
# longitud_nombre = len(nombre)
# for i in range(longitud_nombre):
#     print(nombre[i])

# Dado  un número que un usuario introduzca por teclado
# y que a través de un for se compruebe si es primo

numero = int(input("Introduce un número \n"))
es_primo = True

for i in range(2, numero):
    if (numero%i==0):
        es_primo = False

if (es_primo):
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")



# for i in range(5):
#     print(i)
#
# for i in range(5,10):
#     print(i)

# for i in range(10, 100, 20):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

