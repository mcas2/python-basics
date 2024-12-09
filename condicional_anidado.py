is_raining = False
humidity = 20
water_mm = 8

if is_raining:
    if water_mm > 4:
        print("Llueve que flipas")
    else:
        print("Chispea")
else:
    if humidity < 20:
        print("Qué seco está el ambiente...")
    elif humidity >= 20 and humidity < 60:
        print("Se está bien")
    else:
        print("Parece que va a llover")