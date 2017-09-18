#encoding:UTF-8
#Autor: Ana María López Soto
#Descripción: Este programa calcula el número remano correspondiente a un número decimal.


#La función calcula el número romano correspondiente al número ingresado
def calcularRomano(numeroUsuario):
    if numeroUsuario == 1  or numeroUsuario ==3 or numeroUsuario ==2:
        numeroRomano = numeroUsuario * "I"
    if numeroUsuario >= 4 and numeroUsuario <= 8:
        numeroRomano = (5 - numeroUsuario) * "I" + "V" + (numeroUsuario - 5) * "I"
    if numeroUsuario == 10:
        numeroRomano = str("X")
    if numeroUsuario ==9:
        numeroRomano = str("IX")
    return numeroRomano


#Lee el numero decimal e imprime resultados
def main():
    numeroUsuario = int(input("Inserte un número entero entre 1 y 10: "))
    if numeroUsuario == 0 or numeroUsuario > 10:
        print("Error, ingrese un valor entre 1 y 10")
    else:
        print("El número romano correspondiente a", numeroUsuario, "es:", calcularRomano(numeroUsuario))
main()



