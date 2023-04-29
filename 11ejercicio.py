def programa():
 n = int(input("Ingrese la cantidad de notas que quiere sacarle el promedio: "))
 suma = 0
 i = 1
 while(i <= n):
    print("Ingrese la nota numero: ",i)
    nota = float(input())
    suma=suma+nota
    i+=1
 prom = suma / n
 print("El promedio de notas es: ",prom)
continuar = input('Desea continuar? S / N :')

if continuar.lower() in "s si y yes":
    programa()
