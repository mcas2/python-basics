import random as r
Matriz = []

for i in range(3):
    Matriz.append([])
    for j in range(3):
        Matriz[i].append(r.randint(0,9))

for i in range(len(Matriz)):
    print(Matriz[i])