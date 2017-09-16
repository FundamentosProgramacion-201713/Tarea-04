#encoding: utf-8
#coded by: Jordan González Bustamante
#Este programa lee la masa de una persona en kg, y su estatura en metros.
#Ademñas calcula su IMC son los datos brindados para finalmente indicarle al usuario en que rango
#se encuentra.

#Esta función verifica que los datos ingresados sean números positivos
def verifyNumber(mass,height):
    return mass <= 0 or height <= 0
#Aquí calculamos el IMC, y su estado según su peso
def calculateIMC(mass, height):
    imc = (mass / height**2)
    if imc < 18.5:
        range = "Bajo peso"
    elif imc >= 18.5 and imc <= 25:
        range = "Peso normal"
    elif imc > 25:
        range = "Sobrepeso"
    return imc, range
#Función principal que llama a las anteriores, además de pedir los datos para su proceso.
def main():
    mass = float(input("Ingrese su masa en Kilogramos (kg) : "))
    height = float(input("Ingrese su estatura en Metros (m) : "))
    if verifyNumber(mass,height) == False:
        imc, range = calculateIMC(mass, height)
        print("Tu IMC es de %.2f, y estás en %s" % (imc, range))
    else:
        print("Datos ingresados inválidos, intente con números reales positivos.")

main()