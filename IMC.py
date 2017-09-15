# encoding-UTF-8
# AUTOR: José Antonio Vázquez Gabián
# Este programa imprime tu indice de masa corporal
#Calcula tu peso y estatura
def calcularIMC (peso,estatura):
    x = (peso)/(estatura**2)
    return x
def saberEstado(imc):
    if imc<18.5:
        p= ("Bajo Peso")
    if imc>=18.5 and imc<=25:
        p= ("Peso Normal")
    if imc>25:
        p= ("Sobrepeso")
    return p
def main(): #se evalua tu rango de estado llamando a la funcion anterior
    Kg=float(input("Teclea tu peso en kilogramos: "))
    M=float(input("Teclea tu estatura en metros: "))
    imc=calcularIMC(Kg,M)
    print("Tu IMC es de: %.2f " % imc)
    rango=saberEstado(imc)
    print("Tu estado es de: " ,rango)
main()