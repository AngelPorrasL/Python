cont=0
saldo = 0
operacion = 0
saldo_nuevo = 0

while cont <= 2:
 print("Escriba su usuario")
 usuario = input()
 print("Escriba su contrasena")
 contrasena = input()
 if usuario.upper() == "ANGELPORRASL" and contrasena.upper() == "ANGELPORRAS2022":
        print("Datos correctos, Bienvenido al Sistema!")

        cont = 3
        respuesta = "si"

        while (respuesta == "si"):
          print("***CAJERO AUTOMATICO***")
          depositar = "A"
          print("Para depositar: Opcion A")
          retirar = "B"
          print("Para retirar dinero: Opcion B")
          ver_saldo = "C"
          print("Para ver su saldo: Opcion C")
          salir = "D"
          print("Para salir: Opcion D")
          yes = False
          opciones = [depositar,retirar,ver_saldo,salir]

          while(not yes):
             print("Selecione lo que quiere hacer")
             opcion = input()
             if opcion.upper() in opciones and opcion.upper() == depositar:
              print("Ha escogido la opcion de deposito")
              yes = True
              yes2 = False

              while(not yes2):
                     print("Digite el monto a depositar")
                     operacion = int(input())
                     deposito = operacion
                     if deposito % 1000 == 0:
                      saldo_nuevo = deposito + saldo
                      saldo = saldo_nuevo
                      print("Ha depositado", deposito,"colones a su cuenta")
                      print("Su saldo actual es de", saldo_nuevo,"colones")
                      yes2 = True
                     else:
                         print("Solo se pueden depositar montos que sean multiplo de 1000")
             elif opcion.upper() in opciones and opcion.upper() == retirar:
              print("Ha escogido la opcion de retirar dinero")
              yes = True
              yes3 = False

              while(not yes3): 
                     print("Digite el monto a retirar")
                     operacion = int(input())
                     retiro = operacion
                     if retiro % 1000 == 0:
                        if retiro < saldo_nuevo:
                          saldo_nuevo = saldo_nuevo - operacion
                          saldo_bancario = saldo_nuevo
                          print("Debido al retiro de dinero su saldo actual es de", saldo_nuevo,"colones")
                        else:
                            print("Saldo insuficiente, no se puede realizar la transaccion")
                        yes3 = True
                     else:
                         print("Solo se pueden retirar montos que sean multiplo de 1000")
             elif opcion.upper() in opciones and opcion.upper() == ver_saldo:
                print("Ha escogido la opcion de ver saldo")
                yes = True
                print("Su saldo actualmente es de",saldo_nuevo,"colones")
             elif opcion.upper() in opciones and opcion.upper() == salir:
              print("Ha escogido la opcion de salir")
              yes = True
             else:
              print("La opcion ingresada no esta en el menu de opciones") 
          print("Quiere hacer algo mas?")
          respuesta = input()   
 else:
  print("Datos incorrectos, intente otra vez")
  if cont == 2:
   print("BLOQUEO DEL SISTEMA")
  cont = cont + 1