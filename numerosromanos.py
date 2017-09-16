#Autor: Mónica Monserrat Palacios Rodríguez
#UTF-8
#Programa para calcular el número romano

def calcularNumeroRomano(n): #Función para Calcular número romano con el parámetro que ingrese el usuario
    if n == 1 or n == 2 or n ==3:
        numeroRomano = ("I"*n)
    elif n == 4:
        numeroRomano = "IV"
    elif n == 5:
        numeroRomano = "V"
    elif n == 6:
        numeroRomano = "VI"
    elif n == 7:
        numeroRomano = "VII"
    elif n == 8:
        numeroRomano = "VIII"
    elif n == 9:
        numeroRomano = "IX"
    else:
        numeroRomano = "X"
    return numeroRomano


def main():#Función principal
    num=float(input("Ingrese un número entre 1 y 10 para convertir a número romano: ", ))#leer el número a convertir
    num = int(num)
    if num >=1 and num<=10: #condición para marcar el error en caso de que se teclee un número que no esté entre el 1 y el 10
        numeroRomano = calcularNumeroRomano(num)#Se llama a la función para calcular el número romano
        print("El número en romano es: ", numeroRomano)
    else:
        print("ERROR, teclee un número entre 1 y 10")

main()#Se llama a la función main
