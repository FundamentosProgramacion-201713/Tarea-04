#encoding: UTF-8
#Autor: Luis Fernando Figueroa Rendon, A01746139
#El programa recibira un numero entre el 1 y el 10 y lo transformara en un numero romano.

#Esta funcion transforma el numero dado a un numero romano.
def convertirRomanos(numero):
    if (numero>=1) and (numero<=3):
        romano= "I" * numero
    elif numero==4:
        romano="IV"
    elif (numero>=5) and (numero<=8):
        romano="V"+"I"*(numero-5)
    elif numero==9:
        romano="IX"
    else:
        romano="X"
    return romano

def main():
    print("")
    numero=int(input("Ingresa un numero del 1 al 10: "))
    print("")
    if (numero<=0) or (numero>10):
        print("Error: Ingrese un numero entre el 1 y el 10.")
    else:
        print("El numero en romano es: ", convertirRomanos(numero))

main()