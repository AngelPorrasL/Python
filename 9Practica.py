palabra1 = input("Escriba la primer palabra: ")
palabra2 = input("Escriba la segunda palabra: ")
 
ult_tres_p1 = palabra1[-3:] 
ult_tres_p2 = palabra2[-3:]
ult_dos_p1 = palabra1[-2:]
ult_dos_p2 = palabra2[-2:]
 
if ult_tres_p1 == ult_tres_p2:
    print("Las palabras riman")
elif ult_dos_p1 == ult_dos_p2:
    print("Las palabras riman un poco")
else:
    print("Las palabras no riman")