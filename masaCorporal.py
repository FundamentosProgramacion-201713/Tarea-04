#encoding: UTF-8
#Autor: Luis Alfonso Alcántara López Ortega, A01374785

#Función para validar los datos
def validarDatos(estatura, peso):
    if estatura <= 0 or peso <= 0:
        return False
    else:
        return True

#Función para calcular el índice de masa corporal
def calcularIMC(estatura, peso):
    imc = peso / (estatura ** 2)
    return imc

#Función para clasificar si está bajo en peso, normal o sobrepeso
def clasificar(imc):
    resultado = ""
    if imc < 18.5:
        resultado = "Bajo peso"
    elif imc >= 18.5 and imc <= 25:
        resultado = "Peso normal"
    elif imc > 25:
        resultado = "Sobrepeso"
    return resultado

def main():

    estatura = float(input("Ingresa la estatura en metros: "))
    peso = float(input("Ingresa el peso en kilogramos: "))
    validacion = validarDatos(estatura, peso)

    if validacion:
        indice = calcularIMC(estatura, peso)
        print("\nÍndice de masa corporal: ", round(indice, 2))
        clasificacion = clasificar(indice)
        print(clasificacion)

    else:
        print("Datos ingresados no válidos")
main()
