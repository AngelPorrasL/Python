l1 = float(input("Escriba el valor del primer lado: "))
l2 = float(input("Escriba el valor del segundo lado: "))
l3 = float(input("Escriba el valor del tercer lado: "))

if(l1==l2 and l2==l3):
  print("\nEl triangulo es equilatero")
elif(l1==l2 or l1==l3 or l2==l3):
  print("\nEl triangulo es isoceles")
elif (l1!=l2 or l1!=l3 or l2!=l3):
 print("\nEl triangulo es escaleno")