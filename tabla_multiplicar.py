tabla = int(input("¿Qué tabla quieres repasar?\n"))
texto = f"aaa{tabla}"

for i in range(10):
    # if (tabla * i == int(input(str(tabla)+"*"+str(i)+": "))):
    if (tabla * i == int(input(f"{tabla}*{i}: "))): 
        print("de lujoo")
    else:
        print(":_(")