print("Ingrese los datos que desea procesar")
N=int(input())
if N > 0 :
    Positivos=int(0)
    Negativos=int(0)
for i in range (N):
    print("Ingrese un numero entero")
    Dato=int(input())
    if Dato > 0:
        Positivos+=1
    elif Dato < 0:
        Negativos+=1
    else:
        print("Digito no valido")
print("La cantidad de numeros positivos fue: ",Positivos,"La cantidad de numeros negativos fue: ",Negativos)