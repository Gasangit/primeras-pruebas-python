def fac(tempf):
    print((int(tempf) - 32) * (0.555))

def caf(tempc):
    print((int(tempc)*1.8)+32)    

print("Este convertidor de unidades de medida de TEMPERATURA le facilitará la conversion de F° a C° y viceversa")

pregunta1=input("¿Que unidad de medida conoce? Ingrese 1 para Fahrenheit o 2 para Celsius: ")

if int(pregunta1) == 1:
    temfac=input("Ingrese la temperatura en F°: ")
    print(fac(temfac))

if int(pregunta1) == 2:
    temcaf=input("Ingrese al temperatura en C°: ")
    print(caf(temcaf))































