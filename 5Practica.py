jornada = 48
print("Escriba el pago por hora")
pagoh = float(input())

print("Escriba las horas extras trabajadas")
horasEx= float(input())
pagoS = pagoh * jornada
totalEx = (pagoh * horasEx)*2
pagoR = pagoS + totalEx

print("Su pago semanal es de: ", pagoS)
print("Sus horas extras son de: ",totalEx)
print("Su pago total es de: ",pagoR)