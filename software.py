#Encoding: UTF-8
#Autor: Eduardo Roberto Müller Romero, A01745219
#Escribe un programa que calcule el descuento dependiendo de las piezas de software que se vendan

def main():
    paquetes = int(input("¿Cuántos paquetes se compraron? "))
    if paquetes <= 0:
        return "Error"
    descuento = calcularDescuento(paquetes)
    pago = calcularPago(paquetes, descuento)
    print("Paquetes comprados:", paquetes)
    print("Descuento:", (descuento * 100), "%")
    print("Total a pagar:", pago)

def calcularDescuento(paquetes):
    if paquetes >= 10 and paquetes <= 19:
        return float(.2)
    elif paquetes >= 20 and paquetes <= 49:
        return float(.3)
    elif paquetes >= 50  and paquetes <= 99:
        return float(.4)
    elif paquetes >= 100:
        return float(.5)
    elif paquetes < 10 and paquetes <= 1:
        return float(0.0)

def calcularPago(paquetes, descuento):
    adescontar = (paquetes * 1500) * descuento
    total  = (paquetes * 1500) - adescontar
    return total

main()