compra = float(input("Ingrese el monto de la compra: "))
if compra <= 10000:
    print("El total a pagar es: ")
elif 10000 <= compra <=  20000:
    compra -= (compra * 0.10)
    print("El total a pagar con su respectivo descuento es: ",compra)
elif 20000 < compra <= 50000:
    compra -= (compra * 0.30)
    print("El total a pagar con su respecivo descuento es: ",compra)
else:
    compra -= (compra * 0.50)
    print("El total a pagar con su respectivo descuento es: ",compra)
