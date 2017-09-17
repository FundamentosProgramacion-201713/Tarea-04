#encoding: UTF-8

# Autor: DiegoArmandoPerezGonzalez, A01374794
# Descripcion: lee numeros romanos entre 1 y 10 y da su traducción en romano

def numRomanoI(numero):
    romano = "I"*numero
    return romano


def numRomanoV(numero):
    if numero == 5:
        numero = "V"
    elif numero == 6:
        numero = "VI"
    elif numero == 7:
        numero = "VII"
    elif numero == 8:
        numero = "VIII"
    return numero


def main():
    numero=int(input("Ingresa un numero entre 1 y 10: "))
    if numero > 10:
        print("numero invalido")
    elif numero >=1 and numero <= 3:
        romano = numRomanoI(numero)
        print("Tu numero es = ", romano)
    elif numero == 4:
        print("IV")
    elif numero >=5 and numero < 9:
        romano2 = numRomanoV(numero)
        print("Tu numero es = ", romano2)
    elif numero==9:
        print("Tu numero es = IX")
    elif numero ==10:
        print("Tu numero es X")

main()