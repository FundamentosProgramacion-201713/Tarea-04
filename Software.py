#AUTOR: GABRIELA MARIEL VARGAS FRANCO A01745775
#endoding: UTF-8
#Lee el número de paquetes y regresa el total a pagar con el descuento correspondiente
costoPaquete=1500

    #Calcula y guarda en la variable totalPagar el total a pagar
def totalPago(paquetesComprados):
#Comparación de datos
    if paquetesComprados<0:
        totalPago=print("Error")
    elif paquetesComprados>=10 and paquetesComprados<=19:
        totalPago=(paquetesComprados*costoPaquete)*.80
    elif paquetesComprados>=20 and paquetesComprados<=49:
        totalPago=(paquetesComprados*costoPaquete)*.70
    elif paquetesComprados>=50 and paquetesComprados<=99:
        totalPago=(paquetesComprados*costoPaquete)*.60
    elif paquetesComprados>=100:
        totalPago=(paquetesComprados*costoPaquete)*.50
    else:
        totalPago=(paquetesComprados*costoPaquete)
#Regresa el totalPago
    return totalPago

def main():
    paquetesComprados=int(input("Número de paquetes comprados:"))
    tP=totalPago(paquetesComprados)
#Imprime el total a pagar
    print("""Total a pagar con descuento es: $""", tP)

main()
