#encoding:UTF-8
#Autor: José Antonio Gómez Mora
#Lee cantidad comprada de paquetes de software e imprime la cantidad descontada y total de la compra.

#calcula el costo total de paquetes con las condiciones dadas para cada rango con el parametro paquetes ingresado por el usuario
def calcularTotal(paquetes):
    total=paquetes*1500
    if paquetes>=10 and paquetes<=19:
        pagoFinal=total*0.80
        return pagoFinal
    elif paquetes>=19 and paquetes<=49:
        pagoFinal=total*0.70
        return pagoFinal
    elif paquetes>=50 and paquetes<=99:
        pagoFinal=total*0.60
        return pagoFinal
    else:
        pagoFinal=total*0.50
        return pagoFinal


def main():
    paquetes=int(input("Ingresa la cantidad de paquetes comprados: "))
    if paquetes>=1:
        total=calcularTotal(paquetes)
        descuentoPorcentaje=-(total/(paquetes*1500))*100+100
        descuentoDinero=paquetes*1500*descuentoPorcentaje/100
        print("El total de descuento de tu compra fue de %d porciento, es decir $%.2f"%(descuentoPorcentaje,descuentoDinero))
        print("El total de tu compra es de: $%.2f"%total)

    else:
        print("Error. Escribe sólo números positivos o mayores que 0.")

main()