#encoding: UTF-8

# Autor: Edgar Alexis González Amador, A01746540
# Descripcion: Programa que permite convertir los numeros digitales del rango 0, 10 en números romanos.

#Esta función convierte el numero digital ingresado a un numero romano.
def convertirDigitalARomano(numeroDigital):
    if numeroDigital > 10:
        mensaje = "Error, debes introducir un valor de 1 a 10"
    elif numeroDigital > 8:
        mensaje = "El número " + str(numeroDigital) + " se escribe " + ((-1 * ((numeroDigital) - 10)) * "I") + "X, en Romano"
    elif numeroDigital > 4:
        mensaje = "El número " + str(numeroDigital) + " se escribe " + "V" + ((numeroDigital - 5) * "I") + ", en Romano"
    elif numeroDigital == 4:
        mensaje = "El número " + str(numeroDigital) + " se escribe IV, en Romano"
    elif numeroDigital > 0:
        mensaje = "El número " + str(numeroDigital) + " se escribe " + (numeroDigital * "I")
    else:
        mensaje = "Error, debes introducir un valor de 1 a 10"
    return mensaje

#Esta función es la función principal del programa, en la que captura los datos e imprime el resultado.
def main():
    numeroDigital = int(input("Introduce el valor en número digital: "))
    mensaje = convertirDigitalARomano (numeroDigital)
    print (mensaje)

main()