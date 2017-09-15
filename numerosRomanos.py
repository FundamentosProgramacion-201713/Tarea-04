#UTF-8
#Autor: Natalia Meraz Tostado          A01745008
#Descripción: leer un número de forma decimal e imprimirlo en número romano

def calcularRomano(decimal):                    #toma el valor decimal para ver que imprimir en romano
    if (decimal >= 1) and (decimal <=3):
        return "I" * decimal
    elif (decimal == 4):
        return "IV"
    elif (decimal ==5):
        return "V"
    elif (decimal >=6) and (decimal <=8):
        return "V" + ("I" * (decimal-5))
    elif (decimal == 9):
        return "IX"
    elif (decimal == 10):
        return "X"
    return "Error"

def main():
    decimal = (int(input("Teclea un número entre 1 y 10: ")))
    print("Número romano: ", (calcularRomano(decimal)))

main()

