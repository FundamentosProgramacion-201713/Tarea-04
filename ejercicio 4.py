# Autor: LuisMiguel Baqueiro
# Matricula: 1745997
#sacar el precio de la cantidad de productos comprados
def calcularDescuento(cantidad, total): #calcula el descuento
    if cantidad >= 10 and cantidad <= 19:
        descuento = total * .2
        return descuento
    elif cantidad >= 20 and cantidad <= 49:
        descuento = total * .3
        return descuento
    elif cantidad >= 50 and cantidad <= 99:
        descuento = total * .4
        return descuento
    else:
        descuento = total * .5
        return descuento
def main():
    cantidad = int(input("Cantidad de paquetes compradas: "))
    if cantidad > 0:
        total = cantidad * 1500
        print("Descuento: $", calcularDescuento(cantidad, total))
        print("Total: $", (total - calcularDescuento(cantidad, total)))
main()