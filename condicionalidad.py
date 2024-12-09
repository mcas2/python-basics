is_raining = True
water_mm = 0.5

if is_raining and water_mm > 0 and water_mm <= 1:
    print("Chispeará")
elif is_raining and water_mm > 1 and water_mm <= 2:
    print("Lleva paragüas")
elif is_raining and water_mm > 2 and water_mm <= 5:
    print("Lleva paragüas y chubasquero")
elif is_raining and water_mm > 5:
    print("Ten cuidado, hay alerta naranja")
else:
    print("Sal tranquilo")

print(f"Van a caer {water_mm} milímetros de agua.")