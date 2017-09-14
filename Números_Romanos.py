#Pedro Cortés Soberanes A01374919
#Función: imprimir el numero romano de cualquier numero decimal entre el 1 y el 10

#Calcular numero romano
def calcularNumRomano (numeroDecimal):
    if numeroDecimal<=3:
        x = ( numeroDecimal * "I")
    else:
        if numeroDecimal==4:
            x = ("IV")
        else:
            if numeroDecimal==5:
                x = ("V")
            else:
                if numeroDecimal>5 and numeroDecimal<=8:
                    x = (("V")+((numeroDecimal%5)*"I"))
                else:
                    if numeroDecimal==9 or numeroDecimal==10:
                        x = (((numeroDecimal % 2) * ("I") + ("X")))
                    else:
                        x=("ERROR, escribe un número que este en el rango entre 1 y 10")

    return x


def main():
    numeroDecimal = int(input("Teclea un número decimal entre el 1 y el 10: "))
    romano = calcularNumRomano(numeroDecimal)
    print(" - El numero en romano es:" ,romano)


main()



