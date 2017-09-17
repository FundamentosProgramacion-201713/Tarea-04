#enconding: UTF-8
#Alejandro Chávez Campos, A01374974
#Este programa es para determinar la el color resultante entre dos colores primarios.

def determinarColor(minusculaColor1, minusculaColor2): #Determina el color resultante
    if (minusculaColor1=="rojo" and minusculaColor2=="azul") or (minusculaColor1=="azul" and minusculaColor2=="rojo"):
        colorResultante= "morado"
        return colorResultante
    elif (minusculaColor1=="rojo" and minusculaColor2=="amarillo") or (minusculaColor1=="amarillo" and minusculaColor2=="rojo"):
        colorResultante="naranja"
        return colorResultante
    elif (minusculaColor1=="azul" and minusculaColor2=="amarillo" ) or (minusculaColor1=="amarillo" and minusculaColor2=="azul"):
        colorResultante="verde"
        return colorResultante
    elif (minusculaColor1=="rojo" and minusculaColor2=="rojo"):
        colorResultante="rojo"
        return colorResultante
    elif (minusculaColor1=="azul" and minusculaColor2=="azul"):
        colorResultante="azul"
        return colorResultante
    elif (minusculaColor1=="amarillo" and minusculaColor2=="amarillo"):
        colorResultante="amarillo"
        return colorResultante


    else:
        colorResultante="Error"
        return colorResultante


def main ():#Programa principal
    color1=str(input("Dame el primer color: "))
    color2=str(input("Dame el segundo color: "))
    minusculaColor1=color1.lower()
    minusculaColor2=color2.lower()
    if ((minusculaColor1=="rojo" or minusculaColor1=="azul") or minusculaColor1=="amarillo") and ((minusculaColor2=="rojo" or minusculaColor2=="azul")or minusculaColor2=="amarillo"):
        colorResultante=determinarColor(minusculaColor1,minusculaColor2)
        print("El resultado de la combinación es: {}".format(colorResultante))
    elif  not(((minusculaColor1=="rojo" or minusculaColor1=="azul") or minusculaColor1=="amarillo") or ((minusculaColor2=="rojo" or minusculaColor2=="azul")or minusculaColor2=="amarillo")):
        print ("Ambos colores no son primarios")
    elif not ((minusculaColor1=="rojo" or minusculaColor1=="azul") or minusculaColor1=="amarillo"):
        print ("El color 1  no es primario")
    elif not ((minusculaColor2=="rojo" or minusculaColor2=="azul")or minusculaColor2=="amarillo"):
        print ("El color 2 no es primario")

main()