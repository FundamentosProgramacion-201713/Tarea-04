#encode: UTF-8
#Autor: Leonardo Castillejos Vite
#Descripción: Un programa en el que el usuario introduce un número del 1-10 y le devuelve su equivalente romano

def main():
    numero = int(input("Escriba su número "))
    if numero >= 1 and numero <= 10:
       romano = convertirRomano(numero)
       print("el número notación romana es: ", romano)
    else:
       print("Valor invalido")

# Convierte un decimal del 1 - 10 en número romano
def convertirRomano (numero):
    if numero <= 3:
        romano = "I" * numero
        return romano
    elif numero == 4:
        romano = "IV"
        return romano
    elif numero == 9:
        romano = "IX"
        return romano
    elif numero == 10:
        romano = "X"
        return romano
    else:
        romano = "V" + ("I" * (numero - 5))
        return  romano

main()