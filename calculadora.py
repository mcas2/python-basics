# Realizar una calculadora
# condicionales -> if
# casteos -> str() int()
# entradas -> input()
# operador -> *, /, + y -
# primer y segundo operandos -> castear, porque entrar como strings
# sacar el resultado

operador = input("Introduce un operador de los siguientes: *, /, + o - \n")

#bucle hasta que se meta un operador correcto
while operador != "*" and operador != "/" and operador != "+" and operador != "-":
    operador = input("Introduce uno correcto\n")

primer_operando = int(input("Introduce el primer número \n"))
segundo_operando = int(input("Introduce el segundo número \n"))

if operador == "*":
    print(primer_operando * segundo_operando)
elif operador == "/":
    print(primer_operando / segundo_operando)
elif operador == "+":
    print(primer_operando + segundo_operando)
elif operador == "-":
    print(primer_operando - segundo_operando)
# else:
#     print("Tu operador no es válido")
