#encoding: UTF-8
#Autor: Luis Alfonso Alcántara López Ortega, A01374785

#Función para calcular el subtotal
def calcularSubtotal(num):
    return num * 1500.0

#Función para validar la entrada
def validarEntrada(num):
    return num >= 0

#Función para calcular el descuento
def calcularDescuento(num):
    if num >= 1 and num <= 9:
        descuento = 0
    elif num >= 10 and num <= 19:
        descuento = 20
    elif num >= 20 and num <= 49:
        descuento = 30
    elif num >= 50 and num <= 99:
        descuento = 40
    elif num >= 100:
        descuento = 50
    else:
        descuento = 0
    return descuento

#Función para calcular el precio
def calcularPrecio(desc, subtotal):
    precio = subtotal * ((100-desc)/100)
    return precio

def main():
    numPaquetes = int(input("Ingresa el número de paquetes: "))
    validacion = validarEntrada(numPaquetes)

    if validacion:
        subtotal = calcularSubtotal(numPaquetes)
        descuento = calcularDescuento(numPaquetes)
        precio = calcularPrecio(descuento, subtotal)
        print("Subtotal: ", subtotal)
        print("Descuento: ", descuento, "%", sep="")
        print("Precio: ", precio)
    else:
        print("Número inválido")

main()