# encoding: UTF-8
#autor: Eduardo Gallegos Solís
#Programa que convierte un número del 1 al 10 en número romano

#Convierte el número decimal leido en romano
def calcularNumeroRomano(numeroDecimal):
    romano = ("ERROR")
    if numeroDecimal>0 and numeroDecimal<=3:
        romano = (numeroDecimal * "I")
    elif numeroDecimal>=4 and numeroDecimal<=8:
        romano = ((4//numeroDecimal * "I") + "V" + (numeroDecimal-5) * "I")
    elif numeroDecimal==9 or numeroDecimal==10:
        romano = ((numeroDecimal%2)*"I" + "X")
    return romano

def main():
    numeroDecimal = int(input("Qué número quieres convertir?: "))
    numeroFinal = calcularNumeroRomano(numeroDecimal)
    print(numeroFinal)

main()