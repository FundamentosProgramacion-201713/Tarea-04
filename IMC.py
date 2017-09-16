#UTF-08
#Autor: Irving Fuentes Aguilera
#Descripción: Programa que calcula el IMC

def calcularIMC(peso, altura):          #Función que calcula el IMC
    imc= peso/(altura**2)
    return imc


def calcularEstado(imc):        #Función que calcula el estado de peso de la persona
    if imc<18.5 and imc>0:
        estado= "Bajo peso"
        return estado
    elif imc>=18.5 and imc<=25:
        estado= "Peso normal"
        return estado
    elif imc>25:
        estado="Sobrepeso"
        return estado
    else:
        estado="Error"
        return estado


def main():
    peso=float(input("Introducir peso:  "))
    altura=float(input("Introducir altura:  "))
    imc=calcularIMC(peso, altura)
    estado=calcularEstado(imc)
    print ("Tu IMC es de:%.2f "% imc)
    print ("Por lo tanto tienes: ", estado)

main()