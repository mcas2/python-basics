# Declarar un nombre correcto
# Pedir al usuario que introduzca su nombre
# Si coinciden, le saludamos, si no, le decimos que es un
# extraño

correct_name = "Alfredo"
user_name = input("Introduce tu nombre: \n")

if correct_name == user_name:
    print(f"Hola, {correct_name}, bienvenid@.")
else:
    print("Identifícate, extraño.")
