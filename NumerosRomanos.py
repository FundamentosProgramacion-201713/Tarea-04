#encoding: UTF-8
#Autor: Ángel Guillermo Ortiz González
#Matrícula: A01745998
#Descripción: Convierte números entre 1 y 10 a números romanos.

#convierte números arábigos entre el 1 y el 10 a su correspondiente número romano
def convertirNumeroARomano(numero):
    if numero >= 1 and numero <= 3:
        romano = numero * "I"
    elif numero >= 4 and numero <=8:
        romano = (5 - numero) * "I" + "V" + (numero - 5) * "I"
    elif numero == 9 or numero == 10:
        romano = (10 - numero) * "I" + "X"
    else:
        romano = 0
    return romano

def main():
    numero = int(input("Inserte un número del 1 al 10: "))
    romano = convertirNumeroARomano(numero)
    print("------------------------------------------")
    if romano == 0:
        print("ERROR. Inserte un número entre 1 y 10.")
    else:
        print("El número romano correspondiente es:",romano)

main()