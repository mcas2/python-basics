alfabeto = [
    "A","B","C","D","E","F","G","H",
    "I","J","K","L","M","N","Ñ","O",
    "P","Q","R","S","T","U","V","W",
    "X","Y","Z"
]

texto = input("Ingrese un texto:\n")
texto = texto.upper()
clave = 2
cifrado = ""
for i in range(len(texto)):
    letraCifrada = alfabeto.index(texto[i]) + clave
    cifrado += alfabeto[letraCifrada]

print(cifrado)
# Pasar un texto y cifrarlo, que nos devuelva el cifrado césar
# Que sea un texto introducido por el usuario, así como una clave introducida
