import time
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def menu_principal(datos):
  clearConsole()
  print("""
        ██████╗░████████╗███╗░░░███╗
        ██╔══██╗╚══██╔══╝████╗░████║
        ██║░░██║░░░██║░░░██╔████╔██║
        ██║░░██║░░░██║░░░██║╚██╔╝██║
        ██████╔╝░░░██║░░░██║░╚═╝░██║
        ╚═════╝░░░░╚═╝░░░╚═╝░░░░░╚═╝
        DINERO A TODO MOMENTO.
  """)
  print ("1 CUENTA DE AHORROS       2 SERVICIO DE GIROS")
  print ("3 SALIR               ") 
  a=input("\nEscoja una opcion valida...   ")

  if a == "1":
    clearConsole()
    menu_cuentaAhorros(datos)
  elif a == "2":
    clearConsole()
    menu_servicioGiros(datos)
  elif a == "3":
    clearConsole()
    mantenimiento(datos)
  else:
    print("No es una opion valida")
    menu_principal(datos)

def menu_cuentaAhorros(datos):
  print("""
      
          █▀▀ █░█ █▀▀ █▄░█ ▀█▀ ▄▀█
          █▄▄ █▄█ ██▄ █░▀█ ░█░ █▀█

          ▄▀█ █░█ █▀█ █▀█ █▀█ █▀█ █▀
          █▀█ █▀█ █▄█ █▀▄ █▀▄ █▄█ ▄█
  """)
  print ("1 RETIRO                  2 CONSULTA DE SALDO")
  print ("3 TRASFERENCIA            4 CANCELAR  ") 
  a= input ("\nEscoja una opcion valida...   ")

  if a=="1":
    clearConsole()
    menu_retiro(datos)
  if a=="2":
    clearConsole()
    menu_consultaSaldo(datos)
  if a=="3":
    clearConsole()
    menu_transferencia(datos)
  if a=="4":
    clearConsole()
    menu_principal(datos)

def menu_retiro(datos):
  print("""
                █▀█ █▀▀ ▀█▀ █ █▀█ █▀█
                █▀▄ ██▄ ░█░ █ █▀▄ █▄█
  """)
  print ("1 100                    2 200")
  print ("3 300                    4 400  ") 
  print ("5 500                    6 600")
  print ("7 Otro Valor             8 CANCELAR  ") 
  a= input("\nEscoja el valor deseado...   ")

  data = datos
  state=0
  if a=="8":
    ope_cancelada() #print ("\nOperacion CANCELADA")
    time.sleep(5)
    menu_principal(datos)
  elif a=="7":
    b= int(input("\nIngrese el valor a retirar (multiplo de 10):   "))
    if (b%10!=0):
      
      print("\nValor no valido   \n")
      ope_cancelada()
      time.sleep(5)
      menu_principal(datos)
    else:
      clave=input("indique la clave de su cuenta:   ")
      for i in range(0, len(datos)):
        #print(f"Clave:{clave} y dato: {data[i][2]}" )
        if clave==data[i][2]:
          saldo = int(data[i][3])
          if(b<saldo):
            saldo -=b
            data[i][3]=saldo
            exitosa() #print ("transacciòn realizada")
            time.sleep(5)
            menu_principal(datos)
          else:
            #print("Saldo no disponible. Operacion cancelada")
            no_disponible()
            time.sleep(5)
            menu_principal(datos)
        else:
          state =1
    clave_incorrecta() if state==1 else print()
    menu_principal()

  else:
    if a=="1":
      b=100
    if a=="2":
      b=200
    if a=="3":
      b=300
    if a=="4":
      b=400
    if a=="5":
      b=500
    if a=="6":
      b=600

    clave=input("indique la clave de su cuenta:   ")
   
    for i in range(0, len(data)):
      #print (data)
      #print(f"Clave:{clave} y dato: {data[i][2]}" )
      if clave==data[i][2]:
        saldo = int(data[i][3])
        if(b<saldo):
          saldo -= b
          data[i][3] = saldo
          exitosa() #print ("transacciòn realizada")
          time.sleep(5)
          menu_principal(datos)
        else:
          #print("Saldo no disponible. Operacion cancelada")
          no_disponible()
          time.sleep(5)
          menu_principal(datos)
      else:
        state=1
    
    clave_incorrecta() if state==1 else print()
  return datos
  menu_principal(datos)

def menu_consultaSaldo(datos):
  print("""
  
          █▀▀ █▀█ █▄░█ █▀ █░█ █░░ ▀█▀ ▄▀█
          █▄▄ █▄█ █░▀█ ▄█ █▄█ █▄▄ ░█░ █▀█

                █▀ ▄▀█ █░░ █▀▄ █▀█
                ▄█ █▀█ █▄▄ █▄▀ █▄█
  """)

  clave=input("indique la clave de su cuenta:   ")
  data = datos
  for i in range(0, len(datos)):
    #print(f"Clave:{clave} y dato: {data[i][2]}" )
    if clave==data[i][2]:
      x=data[i][3]
  print (f"\nSALDO:   {x}")
  time.sleep(3)
  menu_principal(datos)

def menu_transferencia(datos):
  print("""
  
▀█▀ █▀█ ▄▀█ █▄░█ █▀ █▀▀ █▀▀ █▀█ █▀▀ █▄░█ █▀▀ █ ▄▀█ █▀
░█░ █▀▄ █▀█ █░▀█ ▄█ █▀░ ██▄ █▀▄ ██▄ █░▀█ █▄▄ █ █▀█ ▄█
  
  """)
  a,b=0,0
  clave=input("indique la clave de su cuenta:   ")
  data = datos
  for i in range(0, len(data)):
    #print(f"Clave:{clave} y dato: {data[i][2]}" )
    if clave==data[i][2]:
      a=i
      origen= data[i][1]
      x=int(data[i][3])
  print (f"\nSu SALDO disponible para transferencias es:    {x}")
  t=True
  while t:
    monto = int(input("Indique el valor a trandeferir:  "))
    if monto > x :
      print("El valor no puede ser superior al saldo")
      time.sleep(3)
      menu_principal(datos)
    else:
      cuenta = input("Indique el numero de cuenta al cual desea trandefir:   " )
      for j in range(0, len(data)):
        #print(f"Clave:{clave} y dato: {data[i][2]}" )
        if cuenta==data[j][1]:
          b=j
          destino=data[j][1]
          y=int(data[j][3])
      print("\nSe realizar la siguiente tranferencia:  ")
      print(F"""
      |   ORIGEN   |   DESTINO   |   MONTO  |
      |  {origen}  |  {destino}  |  {monto}  |
      """)
      w= input("\nDesea continuar y/n:  ")
      if w=="y" or w== "Y":
        data[a][3]=x-monto
        data[b][3]=y+monto
        t=False
        exitosa()
    menu_principal(data)    
  
def menu_servicioGiros(datos):
  print("""
  
          █▀ █▀▀ █▀█ █░█ █ █▀▀ █ █▀█   █▀▄ █▀▀  
          ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ █ █▄█   █▄▀ ██▄  

                    █▀▀ █ █▀█ █▀█ █▀
                    █▄█ █ █▀▄ █▄█ ▄█
  """)
  a = input("Indique el codigo del giro que desa realizar:  ")

  giros ={"6798":150, "0715":8400, "7803":70, "1105":900}
  v=0
  for i in giros:
    if i == a:
      v=1
  if v==1:
    print(f"\nEl valor del giro que desea realizar es de {giros[a]}")
     
    w= input("\nDesea continuar (y/n):   ")
    if (w=="y" or w=="Y"):
      exitosa()
    else:
      ope_cancelada()
  else:
    print("\nCodigo No Aplica")
    time.sleep(1)
    ope_cancelada()
  time.sleep(5)
  menu_principal(datos)

def mantenimiento(datos):
  interno = {"MANTENIMIENTO": "MANY21M05", "BANCARIA":"BANGR21Y07M"}

  cl= input("Indique la clave de mantenimiento:  ")

  if cl == interno["MANTENIMIENTO"]:
    print("""
    
      ▄▀█ █▀█ ▄▀█ █▀▀ ▄▀█ █▄░█ █▀▄ █▀█  
      █▀█ █▀▀ █▀█ █▄█ █▀█ █░▀█ █▄▀ █▄█  

          █▀ █ █▀ ▀█▀ █▀▀ █▀▄▀█ ▄▀█
          ▄█ █ ▄█ ░█░ ██▄ █░▀░█ █▀█
    """)
    time.sleep(5)
    clearConsole()
    quit()
  elif (cl== interno["BANCARIA"] or cl=="X"):
    print("""
--------------------------------------
|         NUMEROS DE CUENTA          |
--------------------------------------
| CUENTA |  NUMERO  | CLAVE | SALDOS |""")
    for i in range(1,len(datos)-1):
      print (f"|   {datos[i][0]}    | {datos[i][1]:.8} | {datos[i][2]}  | {datos[i][3]} |")
    input("Enter para salir..")
    clearConsole()
    quit()

  else:
    ope_cancelada()
    time.sleep(5)
    menu_principal(datos)

def no_disponible():
  clearConsole()
  print("""
  
        █▀ ▄▀█ █░░ █▀▄ █▀█   █▄░█ █▀█
        ▄█ █▀█ █▄▄ █▄▀ █▄█   █░▀█ █▄█

        █▀▄ █ █▀ █▀█ █▀█ █▄░█ █ █▄▄ █░░ █▀▀
        █▄▀ █ ▄█ █▀▀ █▄█ █░▀█ █ █▄█ █▄▄ ██▄
  
  """)

def ope_cancelada():
  clearConsole()
  print("""
  
          █▀█ █▀█ █▀▀ █▀█ ▄▀█ █▀▀ █ █▀█ █▄░█
          █▄█ █▀▀ ██▄ █▀▄ █▀█ █▄▄ █ █▄█ █░▀█

          █▀▀ ▄▀█ █▄░█ █▀▀ █▀▀ █░░ ▄▀█ █▀▄ ▄▀█
          █▄▄ █▀█ █░▀█ █▄▄ ██▄ █▄▄ █▀█ █▄▀ █▀█
  
  """)

def exitosa():
  clearConsole()
  print("""
  
      ▀█▀ █▀█ ▄▀█ █▄░█ █▀ ▄▀█ █▀▀ █▀▀ █ █▀█ █▄░█
      ░█░ █▀▄ █▀█ █░▀█ ▄█ █▀█ █▄▄ █▄▄ █ █▄█ █░▀█

              █▀▀ ▀▄▀ █ ▀█▀ █▀█ █▀ ▄▀█
              ██▄ █░█ █ ░█░ █▄█ ▄█ █▀█
  
  
  """)

def clave_incorrecta():
  clearConsole()
  print(""" 
  
                 █▀▀ █░░ ▄▀█ █░█ █▀▀  
                 █▄▄ █▄▄ █▀█ ▀▄▀ ██▄  

      █ █▄░█ █▀▀ █▀█ █▀█ █▀█ █▀▀ █▀▀ ▀█▀ ▄▀█
      █ █░▀█ █▄▄ █▄█ █▀▄ █▀▄ ██▄ █▄▄ ░█░ █▀█
  
  """)
  time.sleep(5)