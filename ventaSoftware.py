#encoding: UTF-8

# Autor: DiegoArmandoPerezGonzalez, A01374794
# Descripcion: dependiendo la cantidad de paquetes que el usuario indique, se aplicara un descuento con respecto a la cantidad de paquetes indicada

def descpacks(paquetes, precio):

    desc = 1
    if paquetes <= 0:
        return "Numero invalido de paquetes"
    if paquetes <= 9 and paquetes >= 1:
        total = (paquetes * precio) * desc
        desc = 0
        return total
    elif paquetes <= 19 and paquetes >= 10:
        desc = .80
        total = (paquetes * precio) * desc
        return total

    elif paquetes <= 49 and paquetes >= 20:
        desc = .70
        total = (paquetes * precio) * desc
        return total

    elif paquetes <= 99 and paquetes >= 50:
        desc = .40
        total = (paquetes * precio) * desc
        return total
    elif paquetes >= 100:
        desc = .50
        total = (paquetes * precio) * desc
        return total

def main ():
    paquetes =int(input("Ingresa el numero de paquetes: "))
    precio = 1500
    total = descpacks(paquetes,precio)
    print("Paquetes comprados es de: ", paquetes)
    print("Descuento: $",(precio * paquetes) - total)
    print("Total a pagar: $",total)

main()