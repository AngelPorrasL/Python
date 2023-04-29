print("Menu de Hamburguesas del Oso Hambriento")
SencillaValor20="A"
print(SencillaValor20)
DobleValor25="B"
print(DobleValor25)
TripleValor28="C"
print(TripleValor28)
print("Cual elige?")
Seleccion=input()
if Seleccion.upper()== SencillaValor20:
    Porcentaje= 20*0.05
    total=20+Porcentaje
    print("Usted compro: ",SencillaValor20,"Su total de pago con tarjeta de credito es",total)
elif Seleccion.upper() == DobleValor25:
    Porcentaje2= 25*0.05
    total2=25 + Porcentaje2
    print("Usted compro: ",DobleValor25,"Su total de pago con tarjeta de credito es de: ",total2)
elif Seleccion.upper() == TripleValor28:
    Porcentaje3= 28*0.05
    total3= 28+ Porcentaje3
    print("Usted compro: ",TripleValor28,"Su total de pago con tarjeta de credito es de: ",total3)
else:
    print("Su eleccion no es valida, intente de nuevo")