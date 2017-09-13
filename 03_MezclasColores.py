# encode UTF-8
# Autor: Luis Enrique Neri Pérez
# Descripción: Un programa que lea dos colores primarios (rojo, azul, amarillo) y que imprima el color resultante almezclarlos.

def compararColores(comparacion1, comparacion2): #Función que selecciona el color que se forma juntando otros dos
    red = str("ROJO")
    blue = str("AZUL")
    yellow = str("AMARILLO")
# --------------------------------------------------------------
    if comparacion1 == red and comparacion2 == blue:
        resultado = str("MORADO")
        return resultado
    elif comparacion1 == red and comparacion2 == yellow:
        resultado = str("NARANJA")
        return resultado
    elif comparacion1 == red and comparacion2 == red:
        resultado = str("ROJO")
        return resultado
#--------------------------------------------------------------
    elif comparacion1 == blue and comparacion2 == yellow:
        resultado = str("VERDE")
        return resultado
    elif comparacion1 == blue and comparacion2 == red:
        resultado = str("MORADO")
        return resultado
    elif comparacion1 == blue and comparacion2 == blue:
        resultado = str("AZUL")
        return resultado
# --------------------------------------------------------------
    elif comparacion1 == yellow and comparacion2 == red:
        resultado = str("NARANJA")
        return resultado
    elif comparacion1 == yellow and comparacion2 == blue:
        resultado = str("VERDE")
        return resultado
    elif comparacion1 == yellow and comparacion2 == yellow:
        resultado = str("AMARILLO")
        return resultado
# --------------------------------------------------------------
    else:
        print("ERROR: Ingrese colores primarios")


def main(): #Función principal
    print("COMBINACIONES DE COLORES")
    print("------------------------------------------------")
    color1 = str(input("Ingrese el primer color primario: "))
    color2 = str(input("Ingrese el segundo color primario: "))
    comparacion1 = color1.upper()
    comparacion2 = color2.upper()
    comparaciones = compararColores(comparacion1,comparacion2)

    if comparaciones=="ROJO" or comparaciones=="AZUL" or comparaciones=="AMARILLO" or comparaciones=="VERDE" or comparaciones=="NARANJA" or comparaciones=="MORADO":
        print("------------------------------------------------")
        print("El la combinación entre los colores", comparacion1, "y", comparacion2, "da",comparaciones)
    else:
        pass

main()