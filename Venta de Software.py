#encoding UTF-8
#Omar Israel Galván García A01745810
#Este programa pide el numero de paquetes y calcula su costo con descuento si aplica

def calcularCosto(paquetes):     #Calcula el costo de los paquetes y su descuento, si aplica
    if paquetes >= 10 and paquetes <20:
        costo = (paquetes * 1500)* (0.80)
        return  costo
    elif paquetes >=20 and paquetes <50:
        costo = (paquetes * 1500) * (0.70)
        return costo
    elif paquetes >= 50 and paquetes <100:
        costo = (paquetes * 1500) * (0.60)
        return costo
    elif paquetes >= 100:
        costo = (paquetes * 1500) * (0.50)
        return costo
    else:
        costo = paquetes * 1500
        return costo


def main():                 #Lee el  número de paquetes e imprime el costo total
    paquetes = int(input("Ingrese el número de paquetes: "))
    if paquetes >= 1:
       total =  calcularCosto(paquetes)
       print("El total de compra es:$",total)

    else:
        print("Error! Ingrese un número válido")

main()



