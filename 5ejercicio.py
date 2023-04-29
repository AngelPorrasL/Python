inversion = float(input("Ingrese la cantidad que quiere invertir: "))
interes = float(input("Ingrese el interes anual: "))
años = int(input("Ingrese el número de años que quiere invertir: "))


for x in range(años):
    inversion = inversion * (1 + interes/100)
    print("El capital obtenido por cada año sera de: " + str(round(inversion, 2)))