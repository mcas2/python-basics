import random

necesitan_espabilar = ["Diana","Ismael","Josué","Anthony",
                       "Daniel","Kiara","Adrián"]

han_espabilao = [
    "Wolbert","Randú","Alaa","Juan",
    "Maria José","Fran"]

random.shuffle(necesitan_espabilar)
random.shuffle(han_espabilao)

for i in range(len(han_espabilao)):
    print(f"{necesitan_espabilar[i]} 💕 {han_espabilao[i]}")

print(f"Soldado caído: {necesitan_espabilar[-1]}")

