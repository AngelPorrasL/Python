a=input("Ingrese el nombre del empleado:\n")
b=int(input("Ingrese pago por dia:\n"))
c=int(input("Ingrese dias Trabajados:\n"))
 
pt=b*c
d=0
s=0

print("Pago total\n",pt)
if pt<800.000:
  d=18.500+(0.03*pt)
  print("Pension\n",d)
else:
  if pt>=800.000:
   d=25.000+(0.05*pt)
  print("Pension\n",d)
if pt<800.000:
    s=pt*0.10
    print("Seguro Social\n",s)
else:
    s=pt*0.15
    print("Seguro Social\n",s)
PagoNeto=pt-(d+s)
print("El pago neto del empleado es\n",PagoNeto)