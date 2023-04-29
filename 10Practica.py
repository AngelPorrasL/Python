print("Las opciones de voto son")
candidatoA="A"
print(candidatoA)
candidatoB="B"
print(candidatoB)
candidatoC="C"
print(candidatoC)
print("Por quien desea votar")
voto=input()
if voto.upper()==candidatoA :
    print("Voto por el partido rojo")
elif voto.upper()==candidatoB :
    print("Voto por el partido verde")
elif voto.upper()==candidatoC :
    print("Voto por el partido azul")
else :
    print("Opción erronea")
