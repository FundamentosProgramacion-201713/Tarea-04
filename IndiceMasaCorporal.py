#enconding: UTF-8
#Alejandro Chávez Campos, A01374974
#Este programa es para determinar el IMC.

def calcularIMC(altura, peso):#Calcula el IMC
    imc= peso/(altura**2)
    return imc


def determinarTipoIMC(imc):#Determina el tipo de IMC
    if imc<18.5:
        tipoIMC=("La persona tiene bajo peso")
        return tipoIMC
    elif imc>=18.5 and imc<=25:
        tipoIMC=("La persona tiene peso nomral")
        return tipoIMC
    elif imc>25:
        tipoIMC=("La persona tiene sobrepeso")
        return tipoIMC



def main(): #Programa principal
    peso=float(input("Dame el peso en kilogramos :"))
    estatura= float(input("Dame la estatura en metros :"))
    if estatura==0 or (estatura<0 or peso<0) :
        print ("La estatura no puede ser 0 o pueden haber valores negativos")
    else:
        imc = calcularIMC(estatura, peso)
        print ("El IMC es %.1f kg/m^2"%imc)
        tipoIMC= determinarTipoIMC(imc)
        print (tipoIMC)
main()
