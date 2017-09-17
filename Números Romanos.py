#encoding: UTF-8
#Autor: Eduardo Roberto Müller Romero, A01745219
#Escribir un programa que lea un numero y regrese la expresión del mismo en numeración romana

def main():
    numero = int(input("Escribe un número del 1 al 10: "))
    analisis = analizarnumero(numero)
    convertir = conversionaromano(analisis)
    print(convertir)

def analizarnumero(numero):
    if numero <= 10 and numero >= 1:
        return int(numero)
    elif numero > 10 or numero < 1:
        print("Error")

def conversionaromano(analisis):
    numero  = analisis
    if numero == 5:
        return "V"
    elif numero < 4:
        return (numero * "I")
    elif numero >= 5 and numero < 9:
        return"V", ((numero - 5) * "I")
    elif numero >= 9:
        return (10 - numero) * "I", "X"
main()