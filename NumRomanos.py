# encode UTF-8
# Autor: Luis Enrique Neri Pérez
# Descripción: Un programa que lea números entre 1 y 10 e imprime el número romano correspondiente

def convertirRomano(numero): #Función que selecciona qué número romano corresponde a un arábigo
    if 1<= numero <=3: #1
        romano = (numero * "I")
        return romano

    elif numero == 4:#2
        romano = ("I"+"V")
        return romano

    elif 5<= numero <=8:#3
        romano = ( "V" + (numero - 5)*"I")
        return romano

    elif numero == 9 or numero == 10:#4
        romano = ((numero % 2)*"I" + "X")
        return romano


def main(): #Función principal
    print("NÚMEROS ROMANOS")
    print("------------------------")
    numero = int(input("Ingrese el número entero arábigo entre 1 y 10 que desea convertir: "))
    numeroInt = int(numero)
    if numeroInt == numero and numeroInt>= 1 and numeroInt<=10:#5
        numeroRomano = convertirRomano(numero)
        print("------------------------")
        print("El número",numero, "en romano es",numeroRomano)
    else:#6
        print("------------------------")
        print("ERROR: Digite un número entero entre 1 y 10")


main()
