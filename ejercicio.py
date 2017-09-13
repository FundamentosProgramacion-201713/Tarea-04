# Autor: LuisMiguel Baqueiro
# Matricula: 1745997
# de numero real a romano
def numeroRomano(numero): # convierte a numero romano
    if numero == 1 or numero == 2 or numero == 3:
        return("1" * numero)
    elif numero == 4:
        return("1V")
    elif numero == 5:
        return("V")
    elif numero == 6 or numero == 7 or numero == 8:
        return("V" + ("1" * (numero - 5)))
    elif numero == 9:
        return("1X")
    elif numero == 10:
        return("X")
def main():
    numero = int(input("Escribe un numero del 1 al 10: "))
    if numero >= 1 and numero <= 10:
        print(numeroRomano(numero))
    else:
        print("Error")
main()