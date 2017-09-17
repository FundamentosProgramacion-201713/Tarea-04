# encoding: UTF-8


# Autor: Iván Alejandro Dumas
# Descripción: Este programa convierte de números decimales a números romános mediante dos métodos


#Función que convierte de sistema decimal a sistema romano de numeración (PERSONAL)
def convertirRomano2(num):
    rangeLista = [(16000,"(IV)"),(12000,"(III)"),(8000,"(II)"),(4000,"(I) "),(1000,"M"),(900,"CM"), (500,"D"), (400,"CD"), (100,"C"), (90,"XC"), (50,"L"), (40,"XL"),(10, "X"), (9, "IX"), (5, "V"), (4, "IV"),(1, "I")]
    numRom = ""
    if num in range (1,20000):
        for x, y in (rangeLista):
            while num >= x:
                numRom = numRom + y
                num = num - x
        numRom = numRom
    else:
        numRom = "Valor invalido"
    return numRom

# A CALIFICAR:
#Función que convierte de sistema decimal a sistema romano de numeración
def convertirRomano(num):
    numRom = "IV"
    if num >= 9:
        numRom = "I" * (-(num - 10)) + "X"
    elif num > 4:
        numRom = "V" + (num-5)*"I"
    elif num < 4:
        numRom = "I" * num
    return numRom


def main():
    num = int(input("Número en sistema decimal: "))
    print ("""
––––––––––––––––––––––––––––––––––––––––––––––––––––––––
""")
    if num > 0 and num < 11:
        numRom = convertirRomano(num)
        print("Número en sistema romano :",numRom)
    else:
        print("ERROR: El valor ingresado es invalido")
    numRom2 = convertirRomano2(num)
    print ("PERSONAL - Número en sistema romano :",numRom2)


main()
