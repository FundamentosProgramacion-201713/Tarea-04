#encoding: UTF-8

# Autor: Edgar Alexis González Amador, A01746540
# Descripcion: Programa que calcula el indice de masa corporal e indica si una persona tiene bajo peso, peso normal o sobre peso

#En esta función se calcula el indice de masa corporal a partir del peso y la estatura
def calcularIMC(peso, estatura):
    IMC = peso / (estatura**2)
    return IMC

#En esta función se determina el estado de salud de la persona a partir del indice de masa corporal
def calcularEstadoDeSalud(IMC):
    if IMC > 25:
        mensaje = "Tienes sobre peso"
    elif IMC > 18.5:
        mensaje = "Tu peso es normal"
    elif IMC >= 0:
        mensaje = "Tu peso es bajo"
    else:
        "Hay un error desconocido"
    return mensaje

#Esta función es la función principal del programa, en la que captura los datos e imprime el resultado.
def main():
    peso = float(input("Introduce el peso de la persona en kilogramos: "))
    estatura = float(input("Introduce la estatura en metros: "))
    #En esta parte del programa se verifica que los valores ingresados sean positivos y el valor de la estatura sea diferente de 0
    if peso < 0 or estatura < 0:
        print("Error, debes introducir valores positivos")
        exit()
    if estatura == 0:
        print("Error, la estatura no puede ser 0")
        exit()
    IMC = calcularIMC(peso, estatura)
    mensaje = calcularEstadoDeSalud(IMC)
    print("")
    print("Tu Indice de Masa Corporal es: %.2f"%IMC)
    print(mensaje)

main()