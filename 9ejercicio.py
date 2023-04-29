numerodecita = int(input("Ingresa el numero de citas: "))
pagoporcita = 0
montopagado = 0

if numerodecita <= 3:
    pagoporcita = 200
    montopagado = numerodecita * pagoporcita
elif numerodecita <= 5:
    pagoporcita = 150
    montopagado = ((numerodecita-3)*pagoporcita)+600
elif numerodecita <= 8:
    pagoporcita = 100
    montopagado = ((numerodecita-5)*pagoporcita)+900
elif numerodecita >= 10:
    pagoporcita = 50
    montopagado = ((numerodecita-8)*pagoporcita)+1200
print("Lo que ha pagado por el tratamiento es: ",montopagado)
print("El pago de la cita es: ",pagoporcita)
