#coding: UTF-8
#Autor Aaron Tonatiuh Villanueva Guzmán
#Este programa imprime el resultado de la mezcla de tres colores especificos sin importar su capitalización. Si recibe un color no preestablecido, regresa un mensaje de error.

#Esta función procesa los colores del usuario y procesa el color mezclado. Regresa una string con el resultado.
def mezclarcolor(primercolor,segundocolor):
  if (primercolor == "rojo" and segundocolor == "azul") or (primercolor == "azul" and segundocolor == "rojo"):
    colormezclado="Morado"
  elif (primercolor == "rojo" and segundocolor == "amarillo") or (primercolor == "amarillo" and segundocolor == "rojo"):
    colormezclado="Naranja"
  elif (primercolor == "azul" and segundocolor == "amarillo") or (primercolor == "amarillo" and segundocolor == "azul"):
    colormezclado="Verde"
  else:
    colormezclado="error"
  return(colormezclado)

#Esta función lee dos colores introducidos por el usuario en texto. Es indiferente a capitalización y, a pesar de que lee cualquier color, utiliza a la función mezclar color para determinar si los colores son compatibles o si se debe imprimir un mensaje de error.
def Main():
  primario=input("Ingrese el primer color").lower()
  secundario=input("ingrese el segundo color").lower()
  print(mezclarcolor(primario,secundario))

Main()
