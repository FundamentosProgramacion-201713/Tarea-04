#coding: UTF-8
#Autor: Aaron Tontiuh Villanueva Guzmán
#Este programa hace cosas

def final(var):
  if: var => 1 and <=3
    q=var*"I"
  elif: var ==4
    q=((var-3)*"I")+"V"
  elif: var => 5 and <=8
    q="V"+((var-5)*"I")
  elif: var ==9
    q="V"+((var-8)*"I")
  return(q)

def Main():
  x=int(input("Ingrese cosas"))
  final=funcion(x)
  print(final)

Main()
