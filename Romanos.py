#Javier Pascal A01375925

def convertir_Decimal(numero): # En esta funcion convertimos el numero decimal a numero romano
    if numero < 11 and numero >0:
        if numero >= 9:
            numero_Romano ="I"*(-1*(numero-10))+"X"
        elif numero > 4:
            numero_Romano= "V" +(numero-5)*"I"
        elif numero == 4:
            numero_Romano= "IV"
        elif numero <4:
            numero_Romano= "I"*(numero)
        return numero_Romano
    else:
        print("Numero inválido")
#La función main se encarga de llamar a la otra función y de imprimir el resultado
def main():
    numero=int(input("Dame un numero del 1 al 10:"))
    romano=convertir_Decimal(numero)
    print("El numero ",numero, " decimal es igual al ",romano, " romano")
main()

