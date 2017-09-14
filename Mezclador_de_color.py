#coding: UTF-8
#Autor Aaron Tonatiuh Villanueva Guzmán
#Este programa imprime el resultado de la mezcla de tres colores especificos sin importar su capitalización. Si recibe un color no preestablecido, regresa un mensaje de error.

#Esta función procesa 
def mezclarcolor(primercolor,segundocolor):
  if (primercolor == "rojo" and segundocolor == "azul") or (primercolor == "azul" and segundocolor == "rojo"):
    colormezclado="Morado"
  elif (primercolor == "rojo" and segundocolor == "amarillo") or (primercolor == "blue" and segundocolor == "amarillo"):
    colormezclado="Naranja"
  elif (primercolor == "azul" and segundocolor == "amarillo") or (primercolor == "azul" and segundocolor == "amarillo"):
    colormezclado="Verde"
  else:
    colormezclado="error"
  return(colormezclado)

def Main():
  primario=input("Ingrese el primer color").lower()
  secundario=input("ingrese el segundo color").lower()
  print(mezclarcolor(primario,secundario))

Main()
