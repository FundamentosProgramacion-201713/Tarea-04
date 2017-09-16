#encoding: UTF-8
#Autor: Irving Fuentes Aguilera
#Descripción: Programa que convierte números decimales a romanos


def calcularRomano(numeroDecimal):              #Esta función convierte los números decimales a romanos
    if numeroDecimal<=3:
        numeroDecimal=numeroDecimal * "I"
        return numeroDecimal
    elif numeroDecimal==4:
        numeroDecimal="IV"
        return numeroDecimal
    elif numeroDecimal>=5 and numeroDecimal<9:
        numeroDecimal=numeroDecimal-5
        numeroDecimal= str(numeroDecimal*"I")
        numeroDecimal= "V"+numeroDecimal
        return numeroDecimal
    elif numeroDecimal==9:
        numeroDecimal="IX"
        return numeroDecimal
    elif numeroDecimal==10:
        numeroDecimal="X"
        return numeroDecimal
    else:
        numeroDecimal="Error"
        return numeroDecimal

def main():
    numeroDecimal= float(input("Introducir número: "))
    numeroDecimal= int(numeroDecimal)
    numeroRomano= calcularRomano(numeroDecimal)
    print("El número romano es: ", numeroRomano)


main()