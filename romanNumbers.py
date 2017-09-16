#encoding: utf-8
#coded by: Jordan Gonzalez Bustamante
#Este programa lee un número entre el 1 y el 10, e imprime el número romano correspondiente
#con sus validaciones correspondientes

#convertNumber se encarga de convertir el valor numérico a String romano.
def convertNumber(number):
    if number > 0 and number < 11:
        roman = "IV"
        if number < 4:
            roman = number * "I"
        elif number > 4 and number < 9:
            roman = "V" + (number - 5) * "I"
        elif number > 8:
            roman = "I" * (10 - number) + "X"
    else:
        roman = "no pudo ser procesado porque es número no valido según la selección"
    return roman

#main, función principal que pide el número en decimal, y llama a la otra función.
def main():
    number = int(input("Teclea el un número entre 1-10 : "))
    roman = convertNumber(number)
    print("El número %i en romano es %s" % (number, roman))

main()
