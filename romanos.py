# encoding UTF-8
# Autor: Jaime Orlando López Ramos, A01374696

#Descripción: programa que lea un número del uno al 10 y lo transforme en romano

def transformarNumero(numero):
    if 1<= numero <=3:
        romano = numero * "I"
    elif numero == 4:
        romano = "IV"
    elif 5<=numero<=8:
        romano = "V" + (numero - 5) * "I"
    elif numero == 9:
        romano = "IX"
    elif 9 <= numero <= 10:
        romano = ((10-numero)* "I") + "X"
    else:
        romano = "valor no válido para este programa"
    return romano


def main():
    numero = int(input("Ingrese un número entero del uno al 10: "))
    romano = transformarNumero(numero)
    print("Su número en romano:", romano)


main()





