# Autor: Saul Rodrigo Toral Luna
# Matrícula: A01745007

#   El programa lee el peso de una persona en kilogramos y la estatura en metros para
#   Calcular e imprime el IMC.  (IMC = masa/estatura2)
#   Además de indicar el estado en que se encuentra la persona


# La función calcula el indice de masa corporal de acuerdo a los datos ingresados
def calcularIMC(masa, estatura):
    IMC = masa / (estatura**2)
    return IMC

# La función por medio de comparaciones evalua el IMC para dirigirlo a una categoría
def calcularEstado(IMC):
    if (IMC < 18.5 and IMC > 0):
        estado = "Bajo de peso"
    elif (IMC >= 18.5 and IMC <= 25):
        estado = "Peso Normal"
    elif (IMC > 25):
        estado = "Sobrepeso"
    else:
        estado = "error"
    return estado

#  Función principal para ingresar e imprimir datos
def main():
    print("")
    masa = float(input("Ingresa tu masa en Kilogramos: "))
    estatura = float(input("Ingresa tu altura en metros: "))
    print("")
#   Los datos ingresados son evaluados para mandar un mensaje si es que haay un error
    if masa == 0 and estatura == 0:
        print("Masa y estatura  deben ser distintos a Cero")
    elif masa <= 0:
        print("Masa invalida, debe ser mayor a cero")
    elif estatura == 0:
        print ("Dato invalido: Estatura invalida en ""0")
    elif estatura < 0:
        print("Dato invalido: No existen estatura negativas")
    else:
        IMC = calcularIMC(masa, estatura)
        print("Tu IMC es de: %.2f" % calcularIMC(masa, estatura))
        print("Tu estado es: ",calcularEstado(IMC))
main()
