#encoding: UTF-8

#Autor: Alberto López Reyes
#Descripción: Este programa calcula el estado físico de una persona de acuerdo al cálculo del índice de Masa Corporal
#basándose en el peso en kg y la altura en m otorgados.

#Esta función calcula el índice de Masa Corporal para luego determinar el estado físico de una persona al ser otorgado
#su peso en Kg y altura en m.
def CalcularIMCyEstadoFísico(fltPeso, fltAltura):

    fltIMC = fltPeso/fltAltura**2

    if fltAltura > 0:
        if fltIMC > 0 and fltIMC <= 18.5:
            strEstado = "Bajo peso"
        elif fltIMC > 18.5 and fltIMC <= 25:
            strEstado = "Peso normal"
        elif fltIMC > 25:
            strEstado = "Sobrepeso"
        else:
            print("""===========================""")
            print("""ERROR: NO SE PERMITEN VALORES NEGATIVOS.
EL PROGRAMA TERMINARÁ.""")
            exit()

    else:
        print("""===========================""")
        print("""ERROR: NO SE PERMITE UNA ESTATURA IGUAL A 0.
EL PROGRAMA TERMINARÁ.""")
        exit()

    return strEstado

#Esta función pide y recibe el peso en Kg y la altura en m de una persona para otorgárselos a la función "CalcularIMCyEstadoFísico"
#y de ahí imprimir el estado físico de la persona resultante de dicha función.
def main():
    print("""===========================""")
    print("""Peso en Kg""")
    fltPeso = float(input("Teclea tu peso en Kg: "))
    print("""===========================""")
    print("""Altura en m""")
    fltAltura = float(input("Teclea tu altura en m: "))

    strEstado = CalcularIMCyEstadoFísico(fltPeso, fltAltura)

    print("""===========================""")
    print("Su estado físico es de: "+strEstado)

main()
