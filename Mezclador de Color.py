#encoding UTF-8
#Omar Israel Galván García A01745810
#Pide al usuario 2 colores e imprime su color resultante

def calcularColor(colorUno,colorDos):  #calcula el color resultante con los datos dados
    if (colorUno == "rojo" or colorUno == "amarillo" or colorUno == "azul") and (colorUno == colorDos):
        resultado = colorUno
        return resultado
    if (colorUno == "rojo" and colorDos == "azul") or (colorUno == "azul" and colorDos == "rojo"):
        resultado = "morado"
        return resultado
    elif (colorUno == "rojo" and colorDos == "amarillo") or (colorUno == "amarillo" and colorDos == "rojo"):
        resultado = "naranja"
        return resultado
    elif (colorUno == "azul" and colorDos == "amarillo") or (colorUno == "amarillo" and colorDos == "azul"):
        resultado = "naranja"
        return resultado
    else:
        resultado = "Error! Ingrese un color válido"
        return resultado

def main():   #Lee los colores e imprime el color resultante
    colorUno = str(input("Ingrese el color 1: "))
    colorDos = str(input("Ingrese el color 2: "))
    cUno = colorUno.lower()
    cDos = colorDos.lower()
    resultado  = calcularColor(cUno,cDos)
    print("El color resultante es:",resultado)


main()



