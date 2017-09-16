#encoding: UTF-8
#Autor: Luis Alfonso Alcántara López Ortega, A01374785
#Programa para convertir un número decimal del uno al diez a romano

#Función para validar la entrada del usuario (Debe estar en el rango [1,10]
def validar(num):
    return num <= 10 and num >=1

#Función para convertir un número en el rango [1,10] a romano
def convertirRomano(num):
    if num <= 3 and num >=1:
        return num * "I"
    elif num == 4:
        return "IV"
    elif num <= 8 and num >=5:
        residuo = num % 5
        return "V" + (residuo * "I")
    elif num <= 10 and num >=9:
        resta = 10 - num
        return (resta * "I") + "X"

#Función main donde el usuario realiza las entradas y se imprime el resultado
def main():
    numero = int(input("Ingresa un número entre 1 y 10: "))
    esValido = validar(numero)

    if esValido:
        numeroRomano = convertirRomano(numero)
        print("El número %d en romano es %s" % (numero, numeroRomano))

    else:
        print("Número fuera de rango")

main()