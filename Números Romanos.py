#encoding: UTF-8
#Jean Paul Esquivel Lobato
#Mátricula: A01376152
#Descripción: Convertidor de números romanos.


#convierte números arábigos entre el 1 y el 10 a su correspondiente número romano

def convertirNumeroRom(numero):
    if numero >= 1 and numero <= 3:
        romano = numero * "I"
    elif numero >= 4 and numero <=8:
        romano = (5 - numero) * "I" + "V" + (numero - 5) * "I"
    elif numero == 9 or numero == 10:
        romano = (10 - numero) * "I" + "X"
    else:
        romano = 0
    return romano


#Función principal

def main():
    numero = int(input("Escribe un número del 1 al 10: "))
    romano = convertirNumeroRom(numero)
    print("------------------------------------------")
    if romano == 0:
        print("ERROR. Escribe un número correcto entre 1 y 10.")
    else:
        print("El número que acabas de escribir en romano es:",romano)

main()
