#UTF-8
#Autor: Nazdira Abigail Cerda del Prado A01375428
#Este programa calcula el IMC

#Calcula IMC de la persona
def calcularIMC(masa,estatura):
    imc=masa/(estatura**2)
    return imc

#Indica si la persona tiene bajo peso, peso normal o sobrepeso
def indicarPersona(imc):
    if (imc<18.50):
        return "Persona con bajo peso"
    elif (imc>=18.5 and imc<=25):
        return "Persona con peso normal"
    else:
        if(imc>25):
            return "Persona con sobrepeso"

def main():
    masa=float(input("Ingrese el peso en kg:"))
    estatura=float(input("Ingrese altura en metros:"))
    if (estatura>=1 and masa>=1):
        imc=float(calcularIMC(masa,estatura))
        print("El IMC del usuario es de:",format(imc,".2f"))
        persona=(indicarPersona(imc))
        print(persona)
    else:
        if (estatura<=0 and masa<=0):
            print("ERROR, por favor ingrese números mayores a cero")
main()