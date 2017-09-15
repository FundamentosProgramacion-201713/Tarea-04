#Autor: Joaquin Rios Corvera A01375441
#Encoding: UTF-8

#Este programa lee un número en decimal e imprime la misma cantidad en números romanos


#Esta función asigna un número romano al decimal si este está dentro del rango establecido.
# De lo contrario, marca un error.
def transformarRomano(decimal):
    if 0 < decimal and decimal < 4:
        romanoI = decimal
        romano = romanoI * "I"

    elif decimal < 6:
        romanoI = 5 - decimal
        romano = (romanoI * "I") + "V"
    elif decimal < 9:
        romanoI = decimal - 5
        romano = "V" + (romanoI * "I")
    elif decimal < 11:
        romanoI = 10 - decimal
        romano = (romanoI * "I") + "X"
    else:
        romano = "El número debe tener un valor entre 1 y 10."
    return romano

def main():
    decimal = int(input("Teclea un número entre 1 y 10: "))
    romano = transformarRomano(decimal)
    print(romano)

main()