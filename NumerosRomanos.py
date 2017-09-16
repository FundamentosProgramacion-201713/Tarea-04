# encoding UTF-8
# Autor: Siham El Khoury Caviedes, A01374764

# Descripción: Traducción de números decimales a romanos.

# Calcular y guardar en la variable romano el número romano equivalente al decimal.
def calcularNumeroRomano(decimal):
    if 1 <= decimal <= 3:
        romano = decimal * "I"
        return romano
    elif decimal == 4:
        romano = "IV"
        return romano
    elif 5 <= decimal <= 8:
        resto = decimal - 5
        romano = "V" + resto * "I"
        return romano
    elif decimal == 9:
        romano = "IX"
        return romano
    elif decimal == 10:
        romano = "X"
        return romano


# Función principal.
def main():
    decimal = int(input("Teclea un número entero entre 1 y 10: "))
    if decimal < 1 or decimal > 10:
        print ("Error. Vuelva a correr el programa e inténtelo de nuevo.")
    else:
        romano = calcularNumeroRomano(decimal)
        print ("El número romano equivalente es:", romano)

main()
