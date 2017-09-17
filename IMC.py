#AUTOR: GABRIELA MARIEL VARGAS FRANCO A01745775
#endoding: UTF-8
#Lee el peso de una persona en kilogramos y la estatura en metros
#Calcula y guarda en la variable calcularIndice
def calcularIndice(peso,estatura):
    calcularIndice=peso/(estatura*estatura)
    if calcularIndice<0:
        print("Error")
    return calcularIndice

def main():
    peso=int(input("Peso en kilogramos: "))
    estatura=float(input("Estatura en metros:"))
#Comparacion para identificar su hay algun error
    if estatura<=0:
        print("Error")
        if peso<0:
            print("Error")

    cI=calcularIndice(peso,estatura)
#Imprime el IMC
    print("El  Indice de Masa Corporal es:",format(cI, ".2f"))


    #Comparaciones para saber si tiene bajo peso, peso normal o sobrepeso
    if cI<18.5:
        print("Usted tiene bajo peso")
    elif cI>=18.5 and cI<25:
        print("Usted tiene un peso normal")
    else:
        print("Usted tiene sobrepeso")
main()
