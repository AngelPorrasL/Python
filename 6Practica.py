def calcular_longitud_cadena(cadena):
  contador = 0
  for c in cadena:
    contador += 1 
  return contador 
texto = "Hola como esta"
print(len(texto))
print(calcular_longitud_cadena(texto))