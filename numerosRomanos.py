#encoding: UTF-8

#Autor: Roberto Téllez Perezyera
"""
Este programa puede leer un número decimal entre el 1 y el 10 y devolver el número correspondiente en romano.
"""


#Una función que recibe el número en decimal y regresa el número romano
def convertirDecimalARomano(numero) :
    if numero == 10 :
        return "X"
    if numero <= 3 :
        return numero * "I"
    if numero == 5 :
        return "V"
    if numero > 3 and numero < 5 :
        return "IV"
    if numero > 8 and numero < 10 :
        return "IX"
    if numero > 5 and numero < 9 :
        unos = numero - 5
        return "V", unos * "I"


#Pedir número decimal al usuario e imprimir número romano o mensaje de error
def main():
    global numeroRomano
    numero = int(input("Escribe tu número favorito del 1 al 10: "))
    if numero > 10 or numero < 1 :
        print ("... del 1 al 10, por favor")
    else :
        numeroRomano = convertirDecimalARomano(numero)
    print (numero, ("en romano es: "), numeroRomano)


main()
