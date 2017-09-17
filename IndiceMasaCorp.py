#Autor: Maria Fernanda Torres Velazquez A01746537
#El programa calcula el IMC de una persona en base a su peso y estatura e indica el estatus del IMC

#Recibe los valores de masa y estatura y devuelve el valor de IMC
def calcularIMC(masa,altura):
    imc= masa/(altura**2)
    return imc

#Recibe el valor de IMC, lo compara y devuelve el estatus
def calcularRango(imc):
    if imc<18.5:
        g =("BAJO PESO")

    elif imc >=18 and imc <=25:
        g= ("PESO NORMAL")

    elif imc>25:
        g= ("SOBREPESO")

    return g

#Funcion principal
def main ():
    print ("BIENVENIDO A LA CALCULADORA DE INDICE DE MASA CORPORAL")
    masa= (float(input(   "Por favor introduce tu masa en kg: ")))
    estatura=(float(input("Por favor introduce tu estatura en metros: ")))
    if masa>0 and estatura>0:
        imc=calcularIMC(masa,estatura)
        rango= calcularRango (imc)
        print ("TU IMC ES: %.2f" %(imc))
        print ("---------------")
        print ("ESTATUS: ",rango)

    else:
        print ("ERROR, LOS VALORES DE MASA Y ESTATURA DEBEN SER MAYORES A 0")



main()

