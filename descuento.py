#encoding: UTF-8
#autor: Juan Sebastian Lozano Derbez
#Descuento

def calculos(packs):
    if packs >= 10 and packs <= 19:
        return (packs * 1500) - ((packs * 1500) * .20)
    elif packs >= 20 and packs <= 49:
        return (packs * 1500) - ((packs * 1500) * .30)
    elif packs >= 50 and packs <= 99:
        return (packs * 1500) - ((packs * 1500) * .40)
    elif packs >= 100:
        return (packs * 1500) - ((packs * 1500) * .50)

def main():
    packs = int(input("Cuántos paquetes desea comprar?: "))

    print("El Total es de: $", calculos(packs))

main()