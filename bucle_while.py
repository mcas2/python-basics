# Bucle que no permita avanzar si el usuario no introduce la
# contraseña correcta declarada en una variable

contraseña = "123"
user_input = input("Escribe la contraseña\n")

while contraseña != user_input:
    user_input = input("Has fallado, introduce la contraseña otra vez\n")

print("Has acertado")