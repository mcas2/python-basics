#print(chr(180))
#mesesConTreintaDias = ["abril", "junio", "septiembre"]
#print("febrero" in mesesConTreintaDias)
#
#mesesConTreintaDias.append("noviembre")
#
#listaNumeros = []
#for i in range(10):
#    listaNumeros.append(int(input(f"Mete el número {i}:\n")))
#
#print(listaNumeros)

def validarDiaSemana(diaSemana):
    while diaSemana.lower() not in ["lunes", "martes", "miércoles", "miercoles", "jueves", "viernes"]:
        diaSemana = input("Introduce un día correcto\n")
    return diaSemana

diaSemana = validarDiaSemana(input("Dime un día de la semana\n"))
print(diaSemana)












