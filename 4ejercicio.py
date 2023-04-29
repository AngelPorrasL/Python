print("Cuantos empleados trbajan en su empresa")
Empleados=int(input())
Mayor=int(0)
Menor=int(0)
for i in range(Empleados):
    print("Digite el pago de los empleados")
    Pago=int(input())
    if Pago >= 1500:
        Mayor += 1
    elif Pago < 1500:
        Menor += 1
    else:
        print("El pago es menos de lo posible") 
print("La cantidad que gana mas de 1500 es: ",Mayor,"La cantidad que gana menos de 1500 es:",Menor)