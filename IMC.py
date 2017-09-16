#Javier Pascal Flores A01375925

def Calcular_imc(peso, altura): #Esta funcion es para calcular el imc
    imc=round((peso/(altura**2)),2)
    return imc
def main(): #Aqui hacemos lo demas, leemos datos, imprimimos y estan las condiciones para decir los deciles
    altura=float(input("Dame tu estatura en metros: "))
    peso = float(input("Dame tu peso en kilogramos: "))
    if altura < 0:
        print("No se aceptan valores negativos")
    elif peso < 0:
        print("No se aceptan valores negativos")
    else:
        imc=Calcular_imc(peso,altura)
        print("Tu IMC es: ",imc)
        if imc < 18.5:
            print("Estas Bajo de Peso")
        elif imc >= 18.5 and imc <25:
            print("Estas en tu peso normal")
        elif imc > 25:
            print ("Tienes sobrepeso")

main()


