#AUTOR: JOSÉ HEINZ MÖLLER SANTOS
#Este programa cambia de numeros normales a numeros romanos del 1 al 10.

def cambiarDecimalARomano(numeroDecimal):

    if numeroDecimal > 10 or numeroDecimal < 0:
        numeroR = "Use del 1 al 10"
    else:

        if numeroDecimal >= 0 and numeroDecimal <= 3:
            numeroR = "I"


        else:
            if numeroDecimal >= 4 and numeroDecimal <= 8:
                numeroR = "V"


            else:
                if numeroDecimal >= 9 and numeroDecimal <= 10:
                    numeroR = "X"
    return numeroR

def agregarValorRI(numeroR,numeroDecimal):
    if numeroR == "I" and numeroDecimal == 1:
        numeroR1 = 1*numeroR
    else:
        if numeroDecimal == 2:
            numeroR1 = 2*numeroR
        else:
            if numeroDecimal == 3:
                numeroR1 = 3*numeroR
    return numeroR1

def agregarValorRV(numeroR,numeroDecimal):

    if numeroR == "V" and numeroDecimal == 5:
        numeroR1 = 1*numeroR
    else:
        if numeroDecimal == 4:
            numeroR1 = "I"+numeroR
        else:
            if numeroDecimal == 6:
                numeroR1 = numeroR + "I"
            else:
                if numeroDecimal == 7:
                    numeroR1 = numeroR + "II"
                else:
                    if numeroDecimal == 8:
                        numeroR1 = numeroR +"III"
    return numeroR1

def agregarValorRX(numeroR,numeroDecimal):
    if numeroR == "X" and numeroDecimal == 10:
        numeroR1 = 1*numeroR
    else:
        if numeroDecimal == 9:
            numeroR1 = "I"+numeroR
        else:
            numeroR1 = "II"+numeroR
    return numeroR1

def sacarNumeroDefinitivo(numeroR,numeroDecimal):
    if numeroDecimal <= 3:
        numeroR1 = agregarValorRI(numeroR,numeroDecimal)
    else:
        if numeroDecimal > 3 and numeroDecimal <= 8:
            numeroR1 = agregarValorRV(numeroR,numeroDecimal)
        else:
            if numeroDecimal >= 9:
                numeroR1 = agregarValorRX(numeroR,numeroDecimal)
    return numeroR1



def main():
    numeroDecimal = int(input("Numero en decimal del 1 al 10: "))
    numeroR = cambiarDecimalARomano(numeroDecimal)
    numeroR1 = sacarNumeroDefinitivo(numeroR,numeroDecimal)
    print("Numero romano: ",numeroR1)

main()

