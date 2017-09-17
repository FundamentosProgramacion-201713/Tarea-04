#Autor: Maria Fernanda Torres Velazquez A01746537
#El siguiente programa lee un numero entero arabigo entre 1 y 10 y lo transforma a numero romano.

#Funcion que recibe el numero arabigo entero, y regresa el valor de numero romano
def transformarNumeros (num):
    if (num >= 1 and num <=3):
        rom= num * "I"

    elif (num == 4):
        rom= "IV"

    elif (num >=5 and num<=8):
        rom= ("V" + (num - 5) * "I")

    elif (num==10):
        rom= "X"

    elif (num == 9):
        rom = "IX"

    return rom

#Funcion principal del programa
def main():
    num= (int(input ("Introduce un numero entre 1 y 10: ")))
    if num>=1 and num<=10:
        rom= transformarNumeros(num)
        print ("El numero %d, en romano es: %s" %(num,rom))

    else:
        print ("ERROR, DEBES INTRODUCIR UN NUMERO ENTRE 1 Y 10")

main()


