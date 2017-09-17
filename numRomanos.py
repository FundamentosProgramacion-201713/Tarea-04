#encoding: UTF-8
#Autor: Daniel Sahuer
#programa que lee un número del 1 al 10 en decimal e imprime su equivalente en número romano


def calcularNumRomano(decimal): #Calcula el número en romano
    if decimal >=1 and decimal<=3:
        n = (decimal * "I")
    elif decimal == 4:
        n = "IV"
    elif decimal == 5:
        n = "V"
    elif decimal >=6 and decimal <=8:
        n = "V" + ((decimal%5) * "I")
    elif decimal >= 9 and decimal <=10:
        n = ("I" * (decimal%2)) + "X"
    else:
        n = "Error"
    return n #regresa


def main():
    numDecimal = int(input("Escribe un número decimal entre el 1 y el 10: "))

    numRomano = calcularNumRomano(numDecimal)

    print ("El número en romano es: ",numRomano)

main()