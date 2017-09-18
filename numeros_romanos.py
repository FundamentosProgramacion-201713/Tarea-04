#encoding: UTF-8
#Autor: Neftalí Rodríguez Martínez, A01375808.
#Lee un número entero entre 1 y 10 e imprime el número romano correspondiente.

def definirRomano(numero): #Calcula el número romano de acuerdo al número decimal.
    if numero >= 1 and numero <= 3:
        numero_romano = numero * "I"
        return numero_romano
    elif numero >=4 and numero <= 5:
        numero_romano = (5 - numero) * "I"
        strRomano = ("{}V".format(numero_romano))
        return strRomano
    elif numero > 5 and numero <= 8:
        numero_romano = (numero - 5) * "I"
        strRomano = ("V{}".format(numero_romano))
        return strRomano
    else:
        numero_romano = (10 - numero) * "I"
        strRomano = ("{}X".format(numero_romano))
        return strRomano

def main (): #Programa principal.
    numero = int(input("Escribe un número entero entre 1 y 10 que desees convertir a número romano: "))
    if numero >= 1 and numero <= 10:
        strRomano = definirRomano(numero)
        print("El número {} equivale a {} ".format(numero, strRomano))
    else:
        print("ERROR, debes escribir un número entero entre 1 y 10")

main()