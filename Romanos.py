# encode: UTF-8
# Autor: David Ramírez Rios; A01338802

#Calcula y convierte un número de entre 1 y 10 a romano
def convertirRomano (decimal):

    if decimal <= 3:
        romano = (decimal * "I")
    elif decimal >= 9:
        if decimal == 10:
            romano = "X"
        else:
            romano = "IX"
    elif decimal == 4:
        romano = "IV"
    elif decimal == 5:
        romano = "V"
    else:
        romano = "V" + (decimal - 5) * "I"


    return romano

def main ():

    decimal = int (input("Escribe el número entero entre 1 y 10 que deseas convertir: "))

    if decimal >= 1  and decimal <=10:
        print(convertirRomano(decimal))
    else:
        print("Error: Número fuera de rango")

main ()