# Generar una contraseña que incluya letras mayúsculas, minúsculas, símbolos y números
# El usuario tiene que dar la longitud de la contraseña
import random as r


def generarContraseña(longitud):
    contraseña = ""
    for i in range(longitud):
        simboloAleatorio = chr(r.randint(32, 126))
        contraseña += simboloAleatorio
    return contraseña

longitudUsuario = int(input("¿Cuántos caracteres quieres que tenga tu contraseña?\n"))
contraseñaDelUsuario = generarContraseña(longitudUsuario)
print(contraseñaDelUsuario)