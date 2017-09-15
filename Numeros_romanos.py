#coding: UTF-8
#Autor: Aaron Tonatiuh Villanueva Guzmán
#Este programa imprime el número romano correspondiente a un número introducido por el usuario. Solamente es capaz de leer números del 1 al 10.

#Esta función lee un número entero proporcionado por Main y procesa el número romano correspondiente. Para reducir las comparaciones, se múltiplica una string.
def crearNumeroRomano(entero):
  if entero <=3:
    q=entero*"I"
  elif entero ==4:
    q=((entero-3)*"I")+"V"
  elif entero <=8:
    q="V"+((entero-5)*"I")
  elif entero ==9:
    q=((entero-8)*"I")+"X"
  elif entero ==10:
    q="X"
  return(q)

#Esta función lee un número introducido por el usuario. Sí dicho número se encuentra en el rango indicado, la función transforma el número en su correspondiente número romano con ayuda de la función crearNumeroRomano. De lo contrario, regresará un mensaje de error.
def Main():
  datosEntrada=int(input("Ingrese un número del 1 al 10"))
  if 1<=datosEntrada<=10:
    print("El número romano correspondiente a", datosEntrada,"es:",crearNumeroRomano(datosEntrada))    
  else:  
    print ("error")

Main()
