#encoding: UTF-8
#Gerardo Arturo Valderrama Quiroz
#A01374994
#Programa que recibe dos colores e indica la combinación que realizan

#Funcion que determina la combinacion de los colores
def definirCombinacion(color1, color2):
    if (color1 == "rojo" and color2 == "amarillo") or (color1 == "amarillo" and color2 == "rojo"):
        return "La combinacion es naranja"
    elif (color1 == "rojo" and color2 == "azul") or (color1 == "azul" and color2 == "rojo"):
        return "La combinacion es morado"
    elif (color1 == "amarillo" and color2 == "azul") or (color1 == "azul" and color2 == "amarillo"):
        return "La combinacion es verde"
    elif (color1 == color2 ):
        return "No hay combinación, el color sigue siendo %s" % color1
    else:
        return "Los colores que diste no son validos"

#Funcion principal main que lee, procesa e imprime datos
def main():
    color1 = (input("Da el color primario 1: ")).lower()
    color2 = (input("Da el color primario 2: ")).lower()
    combinacion = definirCombinacion(color1,color2)
    print(combinacion)

main()