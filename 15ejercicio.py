print("Digite un valor para la altura")
altura=int(input())
for i in range(1,altura+1):
    for columna in range(1,i+1):
     print(columna, end=" ")
    print()