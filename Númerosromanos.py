#encoding: UTF-8

#Autor: Alberto López Reyes
#Descripción: Este programa imprime el número romano equivalente de un número decimal otorgado.

#Esta función define el número romano de acuerdo al número decimal otorgado.
def DefinirNumeroRomano(intNumDecimal):
    if intNumDecimal > 0 and intNumDecimal <= 10:
        if intNumDecimal / 1 == 1 or intNumDecimal / 6 == 1 or intNumDecimal / 4 == 1:
            strNumRomano = "I"
        elif intNumDecimal / 2 == 1 or intNumDecimal / 7 == 1:
            strNumRomano = "II"
        else:
            strNumRomano = "III"

        if (intNumDecimal + 1) / 5 == 1:
            strNumRomano = strNumRomano + "V"
        elif intNumDecimal / 5 == 1:
            strNumRomano = "V"
        elif intNumDecimal >= 6 and intNumDecimal < 9:
            strNumRomano = "V" + strNumRomano
        elif intNumDecimal == 9:
            strNumRomano = "IX"
    else:
        print("""===========================""")
        print("""ERROR: EL RANGO DE NÚMEROS DECIMALES VALIDOS ES DEL 0 AL 10.
EL PROGRAMA TERMINARÁ.""")
        exit()

    return strNumRomano

#Esta función pide y recibe un número decimal para otorgárselo a la función "DefinirNumeroRomano" para así
#imprimir el número romano equivalente calculado en dicha función.
def main():
    print("""""")
    print("""===========================""")
    print("Número Decimal")
    intNumDecimal = int(input("Teclea el número decimal: "))
    print("""===========================""")
    print("Número Romano")

    strNumRomano = DefinirNumeroRomano(intNumDecimal)

    print("El número romano equivalente es: "+strNumRomano)

main()