#encoding:UTF-8
#Autor: José Antonio Gómez Mora
#El usuario ingresa un numero entre 1-10 y el programa regresa el número en romano

#Calcula el número romano con el parametro del número decimal ingresado por el usuario
def calcularRomano(nDecimal):
    if nDecimal>=1 and nDecimal<=3:
        return (nDecimal*"I")

    elif nDecimal==4:
        return("IV")
    elif nDecimal>=5 and nDecimal<=8:
        return ("V"+(nDecimal-5)*("I"))
    else:
        return((10-nDecimal)*("I")+("X"))


def main():
    nDecimal=int(input("Teclea un número entre 1 y 10: "))
    if nDecimal>=1 and nDecimal<=10:
        nRomano=calcularRomano(nDecimal)
        print("El número %d equivale en romano a:"%nDecimal,nRomano)


    #si el número ingresado por el usuario es menor que 0, imprime mensaje de error.
    elif nDecimal<0:
        print("Escribe un número positivo.")

    #si el número que ingresa el usuario esta fuera de rango, imprime error.
    else:
        print("Escribe un número dentro del rango.")


main()

