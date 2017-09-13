def cambiarDecimalARomano(numeroDecimal):
    if numeroDecimal > 10 or numeroDecimal < 0:
        numeroR = "No uses numeros menores a 0 o mayores a 10"
        return numeroR
    else:
        if numeroDecimal == 1:
            numeroR = "I"
        else:
            if numeroDecimal == 2:
                numeroR = "II"
            else:
                if numeroDecimal == 3:
                    numeroR = "III"
                else:
                    if numeroDecimal ==4:
                        numeroR = "IV"
                    else:
                        if numeroDecimal == 5:
                            numeroR = "V"
                        else:
                            if numeroDecimal == 6:
                                numeroR = "VI"
                            else:
                                if numeroDecimal == 7:
                                    numeroR = "VII"
                                else:
                                    if numeroDecimal == 8:
                                        numeroR = "VIII"
                                    else:
                                        if numeroDecimal == 9:
                                            numeroR = "IX"
                                        else:
                                            if numeroDecimal == 10:
                                                numeroR = "X"

    return numeroR

def main():
    numeroDecimal = int(input("Numero en decimal del 1 al 10: "))
    numeroRomano = cambiarDecimalARomano(numeroDecimal)

    print("Numero Romano: ", numeroRomano)

main()