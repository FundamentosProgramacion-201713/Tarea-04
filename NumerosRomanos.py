#encoding: UTF-8
# Autor: Dora Gabriela Lizárraga González - A01229599
# Este programa lee un número decimal y el programa regresa su equivalente en número romano.

# Esta función calcula el equivalente romano dependiendo del rango en el que se encuentre el número introducido.
def calcularRomano (numeroDecimal):
    decimal = numeroDecimal
    if decimal <= 3:
        roman = decimal*"I"
    elif decimal ==4:
        roman = "IV"
    elif 5 <= decimal <= 8:
        roman = "V" + ((decimal-5)*"I")
    else:
        roman = ((decimal%2)*"I")+"X"
    return roman

# Esta función lee los valores de las variables, ejecuta las otras funciones e imprime el resultado.
def main():
    numeroDecimal= int(input("Introduzca un número entre 1 y 10 para conocer su equivalente romano: "))
    print()
    if 1 <= numeroDecimal <= 10:
        roman = calcularRomano(numeroDecimal)
        print("El equivalente del número", numeroDecimal, "en romano es: ", roman)
    else:
        print("El número introducido es inválido.")

main()