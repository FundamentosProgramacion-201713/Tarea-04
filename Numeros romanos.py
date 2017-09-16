#Encoding: UTF-8
#Autor: Luis Daniel Rivera Salinas  A01374997
#Descripcion: Convierte numeros decimales a romanos, de entre 1 y 10

def obtenerNumeroRomano(numero): #Multiplica el numero para obtener el I
    return "I"*numero

def obtenerNumeroRomanoMayor4(numero): #Decide si el numero es entre 4 o 5
    if numero==4:
        return "IV"
    else:
        return "V"

def main(): #decide si el numero es menor o igual a 10, y mayor o igual a 1, para conversion
    numero = int(input("Ingresa un numero: "))
    if numero >= 1 and numero <= 10:
        if numero <4:
            numeroRomano = obtenerNumeroRomano(numero)
            print("Tu numero en romano es ", numeroRomano)
        elif numero <9 :
            numeroRomano = obtenerNumeroRomanoMayor4(numero)
            numero = numero-5
            numero = obtenerNumeroRomano(numero)
            print("Tu numero en romano es ",numeroRomano,numero)
        elif numero == 9:
            print("Tu numero en romano es IX" )
        else:
            print("Tu numero en romano es X")
    else:
        print("Error, numero ingresado no valido")
main()
