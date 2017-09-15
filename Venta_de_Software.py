#Pedro Cortés Soberanes A01374919
#Función: calcular precio de paquetes con descuento


#Calcular precio del rectangulo con descuento
def calcularPrecio (paquetes):
    if paquetes<10:
        x= paquetes*1500
    else:
        if paquetes>=10 or paquetes<=19:
            x = (paquetes*1500)-((paquetes*1500)*(.20))
        else:
            if paquetes>=20 or paquetes<=49:
                x = (paquetes*1500)-((paquetes*1500)*.30)
            else:
                if paquetes>=50 or paquetes<=99:
                    x = (paquetes*1500)-((paquetes*1500)*.40)
                else:
                    if paquetes>=100:
                        x = (paquetes*1500)-((paquetes*1500)*.50)
                    else:
                        if paquetes<0:
                            x = ("ERROR")
    return x


def main():
    numPaquetes= float(input("Teclea el número de paquetes: "))
    precioConDescuento = calcularPrecio(numPaquetes)
    print ("""
- El precio de los paquetes con descuento es: """, precioConDescuento)


main()