# encoding: UTF-8
# Viviana Osorio Nieto
# calcular el numero romano de 1 al 10.
#calcular el numero en romano
def calcularRomano(a):
    if a < 4:
        r = (a * "I")
    else:
        if a == 4:
            r = "IV"
        else:
            if a == 5:
                r = "V"
            else:
                if a < 9:
                    r = "V" + ((a - 5) * "I")
                else:
                    if a == 9:
                        r = "IV"
                    else:
                        if a == 10:
                            r = "X"
                        else:
                            if a > 10:
                                r = "error"

    return r

#funcion principal. leer imprimir vaalores
def main():
    strT = int(input("ingrese un numero del 1 al 10: "))
    a = strT

    x = calcularRomano(a)

    print("el numero es: ", x)


main()

