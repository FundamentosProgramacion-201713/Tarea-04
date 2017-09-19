#UTF-8
#Autor: Nazdira Abigail Cerda del Prado A01375428
#Calcula cantidad a pagar y cantidad descontada en la venta

#Calcula en descuento aplicado
def calcularDescuento(softwarecomprado):
    if (softwarecomprado>=1 and softwarecomprado<=18):
        descuento=(softwarecomprado*1500)-(softwarecomprado*1500)
    elif (softwarecomprado <= 19 and softwarecomprado >= 10):
        descuento= (softwarecomprado*1500)-((softwarecomprado * 1500) -(softwarecomprado*1500*.20))
    else:
        if(softwarecomprado<= 49 and softwarecomprado>=20):
            descuento= (softwarecomprado*1500)-((softwarecomprado*1500)-(softwarecomprado*1500*0.30))
        else:
            if(softwarecomprado >= 50 and softwarecomprado<= 99):
                descuento =(softwarecomprado*1500)- ((softwarecomprado*1500)-(softwarecomprado*1500*0.40))
            else:
                if(softwarecomprado>=100):
                    descuento = (softwarecomprado*1500)-((softwarecomprado*1500)-(softwarecomprado*1500*0.50))
    return descuento

#Calcula en total a pagar con descuento
def calcularTotalconDescuento(softwarecomprado):
    if (softwarecomprado>=1 and softwarecomprado<=18):
        pagar=(softwarecomprado*1500)
    elif (softwarecomprado <= 19 and softwarecomprado >= 10):
        pagar = (softwarecomprado * 1500) -(softwarecomprado*1500*.20)
    else:
        if(softwarecomprado<= 49 and softwarecomprado>=20):
            pagar = (softwarecomprado*1500)-(softwarecomprado*1500*0.30)
        else:
            if(softwarecomprado >= 50 and softwarecomprado<= 99):
                pagar = (softwarecomprado*1500)-(softwarecomprado*1500*0.40)
            else:
                if(softwarecomprado>=100):
                    pagar = (softwarecomprado*1500)-(softwarecomprado*1500*0.50)

    return pagar

def main():
    softwarecomprado=float(input("Paquetes comprados:"))
    if (softwarecomprado>=1):
        descuentosoft = float(calcularDescuento(softwarecomprado))
        totalpagar = float(calcularTotalconDescuento(softwarecomprado))
        print ("Por", softwarecomprado, "paquetes:")
        print("Descuento aplicado:", format(descuentosoft,".2f"),"pesos")
        print("TOTAL A PAGAR:", format(totalpagar,".2f"), "pesos")
    else:
        if (softwarecomprado<=0):
            print("Error por favor ingrese números positivos mayores a cero")

main()