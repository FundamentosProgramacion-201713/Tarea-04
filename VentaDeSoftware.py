# encoding UTF-8
# Autor: Siham El Khoury Caviedes, A01374764

# Descripción: Cálculo del descuento en la venta de software.

# Calcular y guardar en la variable descuento la cantidad descontada.
def calcularDescuento(paquetes, costo):
    if 10 <= paquetes <= 19:
        descuento = costo * .20
        return descuento
    elif 20 <= paquetes <= 49:
        descuento = costo * .30
        return descuento
    elif 50 <= paquetes <= 99:
        descuento = costo * .40
        return descuento
    elif paquetes >= 100:
        descuento = costo * .50
        return descuento
    elif paquetes < 10:
        descuento = 0
        return descuento


# Calcular y guardar en la variable costoTotal el costo total a pagar.
def calcularCostoTotal(costo, descuento):
    costoTotal = costo - descuento
    return costoTotal


# Función principal.
def main():
    paquetes = int(input("Número de paquetes comprados: "))
    if paquetes < 0:
        print ("Error, la cantidad de paquetes comprados no es válida.")
    else:
        precio = 1500
        costo = paquetes * precio
        descuento = calcularDescuento(paquetes, costo)
        costoTotal = calcularCostoTotal(costo, descuento)
        print ("Cantidad descontada: $ %.2f" % descuento)
        print("Total a pagar: $ %.2f" % costoTotal)

# Ejecutar función principal.
main()
