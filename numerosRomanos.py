#Encoding: UTF-8
#Autor: Angel Roberto Pesado Bartolo  A01374942
#Descripcion: El codigo pregunta al usuario un numero del 1 al 10 e imprime el numero en romano.

def obtenerNumeroRomanoMenor(num): #La función multiplica el numero de veces por I
    numero="I"*num
    return numero

def obtenerNumeroRomanoMayor(num): #La función determina si es el numero 4 o 5
    if num==4:                   #Si el numero es cuatro
        return "IV"                #Regresa IV
    else:
        return "V"                 #Regresa V

def main():                     #definimos la función main
    numero = int(input("Teclea un numero del 1 al 10: ")) #Pedimos al usuario el numero
    if numero >= 1 and numero <= 10:
        if numero <4:
            numerom = obtenerNumeroRomanoMenor(numero)
            print("Tu numero que tecleaste, en romano es: ", numerom)
        elif numero <9 :
            numerorma = obtenerNumeroRomanoMayor(numero)
            numero = numero-5
            numero = obtenerNumeroRomanoMenor(numero)
            print("Tu numero que tecleaste, en romano es: ",numerorma,numero)
        elif numero == 9:
            print("Tu numero que tecleaste, en romano es: IX" )
        else:
            print("Tu numero que tecleaste, en romano es: X")
    else:
        print("Error, el numero no esta en en rango indicado")
main()     #Llamamos a la funcion main para que realice lo que  tiene dentro de ella
