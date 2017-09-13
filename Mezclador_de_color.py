def mezcladordecolor(primercolor,segundocolor):
  if (primercolor == "rojo" or primercolor=="azul") and (segundocolor=="rojo" or segundocolor=="azul"):
    x="Morado"
  elif (primercolor == "rojo" or primercolor=="amarillo") and (segundocolor=="rojo" or segundocolor=="amarillo"):
    x="Naranja"
  elif (primercolor == "azul" or primercolor=="amarillo") and (segundocolor=="azul" or segundocolor=="amarillo"):
    x="verde"
  return(x)

def Main():
  primario=input("Ingrese el primer color").lower()
  secundario=(input("ingrese el segundo color")).lower()
  coloresaceptados ="rojo","azul","amarillo"
  if (primario== coloresaceptados) and (secundario==coloresaceptados):
    print(mezcladordecolor(primario,secundario))
  else:
    print("error")
Main()
