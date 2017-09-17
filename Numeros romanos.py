# Autor: Saul Rodrigo Toral Luna
# Matrícula: A01745007

# El programa  lee un número entre 1 y 10 que ingresa el usuario
# E imprime el número romano correspondiente


# La función por medio de operaciones y comparaciones
# Calcula el número romano de acuerdo al dato ingresado
def calcularRomano(numero):
    if numero <= 3:
        romano = numero * "I"
    elif numero == 4:
        romano = "IV"
    elif numero <= 8:
        romano = "V" + (numero-5)*"I"
    elif numero == 9:
        romano = "IX"
    else:
        romano = "X"
    return romano

# Función principal para ingresar e imprimir datos
def main():
    print("")
    print("Convertir números arabigos a romanos")
    print("")
    numero = int(input("Ingresa un número entre 1 y 10: "))
# Si el número está fuera de los parametros de 1 a 10 manda un error
    if numero > 0 and numero < 11:
        print("")
        print("El número", numero, "en romano es: ",calcularRomano(numero))
    else:
        print(numero, "Es un dato invalido, la escala debe ser entre 1 y 10")


main()
