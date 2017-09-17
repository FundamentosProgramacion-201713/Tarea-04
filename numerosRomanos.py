#encoding: UTF-8
#Autor: Sebastian Morales Martin
#Tarea 4 "if": interpretar un número decimal a número romano
cincoRomano = "V"
diesRomano = "X"


def main():

    numeroDecimal = int(input("Teclee el número decimal de 1 al 10: "))

    if numeroDecimal != [1,10]:
        print("ERROR. Sólo puedes elegir entre el 1 y el 10!")

    numeroRomano = definirNumeroRomano(numeroDecimal)

    print(numeroRomano, "=", numeroDecimal)

    return numeroDecimal



def definirNumeroRomanoI(romano):
    if romano == (1, 4, 6, 9):
        romano = "I"
    return romano

def encontrarNumeroRomanoII(romano):
    if romano == (4, 5, 6, 7, 8):
        romano = cincoRomano + definirNumeroRomanoI(romano)
    return romano

def definirNumeroRomano111(romano):
    if romano == (2, 8):
        romano = encontrarNumeroRomanoII(romano)+ "II"
    return romano

def definirNumeroRomano (romano):
    numeroRomano = definirNumeroRomanoI(romano) + encontrarNumeroRomanoII(
        romano) + definirNumeroRomano111(romano)
    return numeroRomano
main()