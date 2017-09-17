#Autor: Maria Fernanda Torres Velazquez A01746537
#El programa 	lee	el	número	de	paquetes de software comprados	y en base a ello hace un descuento y
# despliega	la cantidad	descontada (si	la	hay) y el total	a pagar	de la compra.

#Funcion que recibe la canidad paquetes de software que desea comprar el usuario y regresa el total sin descuento
def calcularPrecio (numeroSoftware):
    precio = (numeroSoftware*1500)
    return precio

#Funcion que recibe la cantidad de paquetes y calcula el descuento
def calcularDescuento (numeroSoftware):
    precio = (numeroSoftware*1500)
    if numeroSoftware>=1 and numeroSoftware<=9:
        desc = 0
    elif numeroSoftware>=10 and numeroSoftware<=19:
        desc =(precio*.20)
    elif numeroSoftware>=20 and numeroSoftware<=49:
        desc =(precio*.30)
    elif numeroSoftware>=50 and numeroSoftware<=99:
        desc =(precio*.40)
    elif numeroSoftware>=100:
        desc =(precio*.50)

    return desc

#Funcion que recibe el total de paquetes y calcula el total a pagar con descuento
def calcularTotal (numeroSoftware):
    precio = (numeroSoftware*1500)
    if numeroSoftware>=1 and numeroSoftware<=9:
        total= precio
    elif numeroSoftware>=10 and numeroSoftware<=19:
        total = precio-(precio*.20)
    elif numeroSoftware>=20 and numeroSoftware<=49:
        total = precio-(precio*.30)
    elif numeroSoftware>=50 and numeroSoftware<=99:
        total = precio-(precio*.40)
    elif numeroSoftware>=100:
        total = precio-(precio*.50)

    return total

#Funcion principal
def main():
    nSoftware = float(input("Introduzca el número de paquetes de software que desea comprar: "))
    if nSoftware>1:
        subtotal= calcularPrecio(nSoftware)
        descuento=calcularDescuento(nSoftware)
        total= calcularTotal(nSoftware)

        print ("Subtotal: $", subtotal)
        print( "        - $",descuento)
        print ("-------------------")
        print ("Total a pagar: $",(total))
    else:
        print ("ERROR CANTIDAD INVALIDA")


main()




