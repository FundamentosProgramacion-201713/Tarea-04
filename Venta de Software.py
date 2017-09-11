#coding: UTF-8
#Autor: Aaron Tontiuh Villanueva Guzmán
#Este programa calcula el descuento de una transacción según el número de unidades adquiridas. Además, imprime el total a pagar.

def calculartotal(numero):
  if numero <=9
    final=numero* 1500
  elif numero <=19
    final=(numero*1500)*.8
  elif numero <=49
    final=(numero*1500)*.7
  elif numero <=99
    final=(numero*1500)*.6
  elif numero => 100
    final=(numero*1500)*.5
  return(final)
  
def Main():
  paquetes= int(input("Ingrese el número de paquetes adquiridos: "))
  if paquetes <=0
    print("error")
  else:
    print(calculartotal(paquetes))  
Main()
