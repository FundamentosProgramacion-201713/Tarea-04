#encoding: UTF-8
#Autor: Javier Martínez Hernández A01375496
#Descripción: Se imprimiran los numeros romanos del 1 al 10 dependiendo de lo que incerte el usuario



def sacarNumeroRomano1(numeroDado): #se calculan los I para sacar numero del 1 al 3 y 6 al 7
    return "I"*numeroDado


def sacarNumeroRomano2(numeroDado):  #regresa el numero romano 4 y 5
    if numeroDado==4:
        return "IV"
    else:
        return "V"


def main():
    numeroDado=int(input("Ingresa un numero: "))
    if numeroDado>=1 and numeroDado<=10:
        if numeroDado<4:
            numeroRomano=sacarNumeroRomano1(numeroDado)
            print("Tu numero en romano es ",numeroRomano)
        elif numeroDado<9:
            numeroRomano=sacarNumeroRomano2(numeroDado)
            numeroDado=numeroDado-5
            numeroDado=sacarNumeroRomano1(numeroDado)
            print("Tu numero en romano es ",numeroRomano,numeroDado)
        elif numeroDado==9:
            print("Tu numero en romano es IX" )
        else:
            print("Tu numero en romano es X")

    else:
        print("ERROR numero no valido")
main()