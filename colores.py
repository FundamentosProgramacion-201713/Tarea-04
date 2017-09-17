#encoding: UTF-8
#autor: Juan Sebastian Lozano Derbez
#Combinaciones

def combinacion(co1,co2):
#Combinaciones
    if (co1.lower() == "rojo" and co2.lower() == "azul") or (co1.lower() == "azul" and co2.lower() == "rojo"):
        return 1

    elif (co1.lower() == "rojo" and co2.lower() == "amarillo") or (co1.lower() == "amarillo" and co2.lower() == "rojo"):
        return 2

    elif (co1.lower() == 'azul' and co2.lower() == 'amarillo') or (co1.lower() == 'amarillo' and co2.lower() is 'azul'):
        return 3

#Colores iguales
    elif (co1.lower() == 'rojo') and (co2.lower() == 'rojo'):
        return 4

    elif (co1.lower() == 'azul') and (co2.lower() == 'azul'):
        return 5

    elif (co1.lower() == 'amarillo') and (co2.lower() == 'amarillo'):
        return 6

def main():
    co1 = input("1: Azul, rojo o amarillo?: ")
    co2 = input("2: Azul, rojo o amarillo?: ")

    if combinacion(co1,co2) == 4:
        print("El color resultante es Rojo")

    elif combinacion(co1,co2) == 5:
        print("El color resultante es Azul")

    elif combinacion(co1,co2) == 6:
        print("El color resultante es Amarillo")

    elif combinacion(co1,co2) == 1:
        print("El color resultante es Morado ")

    elif combinacion(co1,co2) == 2:
        print("El color resultante es Naranja")

    elif combinacion(co1,co2) == 3:
        print("El color resultante es Verde")

main()