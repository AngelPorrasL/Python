print("Digite un valor para la altura")
altura= int(input())
for i in range(1,altura+1):
    for j in range(altura-i):
        print(" ",end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()