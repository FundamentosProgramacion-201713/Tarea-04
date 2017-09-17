#encoding: UTF-8

# Autor: DiegoArmandoPerezGonzalez, A01374794
# Descripcion: usando los dos colores primarios dados por los usuarios regrese el color resultante o en dado caso error

def mezclacolor(co1min, co2min):
    if co1min == "rojo" and co2min == "rojo":
        return ("Rojo")
    elif co1min == "amarillo" and co2min == "amarillo":
        return ("Amarillo")
    elif co1min == "azul" and co2min == "azul":
        return ("Azul")
    elif (co1min == "rojo" and co2min == "amarillo") or (co1min == "amarillo" and co2min == "rojo"):
        return ("Naranja")
    elif (co1min == "rojo" and co2min == "azul") or (co1min == "azul" and co2min == "rojo"):
        return ("Morado")
    elif (co1min == "azul" and co2min == "amarillo") or (co1min == "amarillo" and co2min == "azul"):
        return ("Verde")
    else:
        return ("Colores no primarios")

def main ():
    co1 = input("color 1: ")
    co2 = input("color 2: ")
    co1min = co1.lower()
    co2min = co2.lower()
    print("Color 1", co1min, ", Color 2", co2min, "Color resultante", mezclacolor(co1min,co2min))

main()