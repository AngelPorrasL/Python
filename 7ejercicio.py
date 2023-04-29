alumnos = int(input("Ingrese la cantidad de alumnos que van a realizar el viaje: "))
 
total, cada_pasaje = 0, 0
 
if alumnos > 100:
    total += 65 * alumnos
    cada_pasaje += 65
elif alumnos >= 50 or alumnos <= 99:
    total += 70 * alumnos
    cada_pasaje += 70
elif alumnos > 30 or alumnos <= 49:
    total += 95 * alumnos
    cada_pasaje += 95
elif alumnos < 30:
    total = 4000
 
print("El costo del pasaje por cada alumno sera de: ", cada_pasaje)
print("El costo del total del viaje sera de: ", total)
