#Autor: Jose Heinz Moller
#Le ponemos software que quiero comprar y nos menciona cuanto cuestan

def calcularDescuentoUtilizado(softwarePaks):
    if softwarePaks <= 9 and softwarePaks >= 1:
        descuento = softwarePaks *1500
    elif (softwarePaks <= 19 and softwarePaks >= 10):
        descuento = (softwarePaks * 1500) -(softwarePaks*1500*.20)
    else:
        if(softwarePaks<= 49 and softwarePaks>=20):
            descuento = (softwarePaks*1500)-(softwarePaks*1500*0.30)
        else:
            if(softwarePaks <= 99 and softwarePaks>= 50):
                descuento = (softwarePaks*1500)-(softwarePaks*1500*0.40)
            else:
                if(softwarePaks>100):
                    descuento = (softwarePaks*1500)-(softwarePaks*1500*0.50)

    return descuento

def main():

    softwarePaks = float(input("¿Cuantas paquetes de Software quieres descargar?: "))
    if (softwarePaks > 0):
        descuentoU = float(calcularDescuentoUtilizado(softwarePaks))

        print(descuentoU)

main()