#encoding UTF-8
#Omar Israel Galván García A01745810
#Este programa lee números del 1 al 10 y devuelve su valor en nímero romano


def imprimirRomano(numero):    #Esta función transforma el  número recibido en romano
    if numero <= 3:
        return (numero * "I")
    elif numero == 4:
        return ("IV")
    elif numero <=8:
        return "V"+((numero-5))*"I"
    elif numero == 9:
        return ("IX")
    else:
        return ("X")

def main():                         #La función principal lee el número decimal
    numero = int(input("Ingrese el número: "))
    if numero >=1 and numero <=10:
     romano = imprimirRomano(numero)
     print(numero,"en romano es",romano)

    else:
        print("Error! Ingrese un valor válido")

main()