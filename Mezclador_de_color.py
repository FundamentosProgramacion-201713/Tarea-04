def mezclarcolor(primercolor,segundocolor):
  if (primercolor == "rojo" or primercolor=="azul") and (segundocolor=="rojo" or segundocolor=="azul"):
    colormezclado="Morado"
  elif (primercolor == "rojo" or primercolor=="amarillo") and (segundocolor=="rojo" or segundocolor=="amarillo"):
    colormezclado="Naranja"
  elif (primercolor == "azul" or primercolor=="amarillo") and (segundocolor=="azul" or segundocolor=="amarillo"):
    colormezclado="Verde"
  else:
    colormezclado="error"
  return(colormezclado)

def Main():
  primario=input("Ingrese el primer color").lower()
  secundario=input("ingrese el segundo color").lower()
  print(mezclarcolor(primario,secundario))

Main()
