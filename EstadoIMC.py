#encoding: UTF-8
# Autor: Dora Gabriela Lizárraga González - A01229599
# Este programa calcula el índice de masa corporal de una persona leyendo su peso y estatura.
# Con este dato puede determinar el estado de la persona respecto a su IMC.

# Esta función calcula el índice de masa corporal con los parámetros que ha introducido el usuario.
def calcularIMC(estatura,peso):
    imc = peso/(estatura**2)
    imc = round(imc,2)
    return imc

# Esta función determina el estado de peso en el que se encuentra el usuario.
def calcularEstado(imc):
    if imc<18.5:
        estado = "peso bajo."
    elif 18.5<=imc<=25:
        estado = "peso normal."
    else:
        estado = "sobrepeso."
    return estado

# Esta función lee los valores de las variables, ejecuta las otras funciones e imprime el resultado.
def main():
    estatura = float(input("Introduzca su estatura en metros: "))
    peso = float(input("Introduzca su peso en kilogramos: "))
    print()
    print("--------------------------------")
    if (estatura<=0) or (peso<0):
        print("Alguno  de los valores que ha introducido es inválido.")
    else:
        imc = calcularIMC(estatura,peso)
        estado = calcularEstado(imc)
        print("Su I.M.C. es de: ",imc)
        print("Usted tiene",estado)

main()