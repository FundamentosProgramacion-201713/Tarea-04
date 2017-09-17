# Autor: Saul Rodrigo Toral Luna
# Matrícula: A01745007

#  El programa lee el número de paquetes comprados
#  E Imprime la cantidad descontada al igual que el total a pagar de la compra


# La función calcula el subtotal a pagar por los paquetes ingresados
def calcularSubTotal(paquetes):
    SubTotal_A_Pagar = paquetes * 1500
    return SubTotal_A_Pagar

# La función calcula el descuento que se aplicará de acuerdo al número de paquetes a comprar
def calcularDescuento(paquetes):
    if paquetes >= 10 and paquetes <= 19:
        descuento = calcularSubTotal(paquetes) * 0.20
    else:
        if paquetes >= 20 and paquetes <= 49:
            descuento = calcularSubTotal(paquetes) * 0.30
        else:
            if paquetes >= 50 and paquetes <= 99:
                descuento = calcularSubTotal(paquetes) * 0.40
            else:
                if paquetes >= 100:
                    descuento = calcularSubTotal(paquetes)* 0.50
                else:
                    if paquetes > 0 and paquetes < 10:
                        descuento = calcularSubTotal(paquetes) * 0
                    else:
                        descuento = "error"
    return descuento

# La función calcula el total a pagar
# Que es el subtotal menos el descuento que le corresponda
def calcularTotal(paquetes):
    total = calcularSubTotal(paquetes) - calcularDescuento(paquetes)
    return total

# Función principal donde ingresa e imprime los datos
def main():
    paquetes = int(input("Ingresa la cantidad de paquetes a comprar: "))
# Determinar si el número de paquetes a comprar es mayor a cero para proceder con las operaciones
    if paquetes > 0:
        print("")
        print("El subtotal a pagar es de $ %.2f" % calcularSubTotal(paquetes))
        print("El descuento que se aplicará en la compra es de: $ %.2f" % calcularDescuento(paquetes))
        print("")
        print("Por la compra de", paquetes,"paquetes", "el monto será de: $ %.2f" % calcularTotal(paquetes), "con el Descuento incluido")
        print("")
    else:
        print("")
        print("Error: Dato invalido para la compra")
main()
