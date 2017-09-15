#encoding: UTF-8
#Especificaciones del programa: Convierte numeros Decimales a romanos
#Autor: Ernesto Ibhar Guevara Gomez
#Matricua: A01746121
def calcularromano(decimal):#Calcula el valor decimal para volverlo romano
    if (decimal>=1)and (decimal<=3):
        return "I"*decimal
    elif (decimal==4):
        return "IV"
    elif (decimal==5):
        return "V"
    elif (decimal>=6)and (decimal<=8):
        return "V" + ("I"*(decimal-5))
    elif (decimal==9):
        return"IX"
    elif (decimal==10):
        return "X"
    return "Error"
def main():
    decimal=int(input("Teclea un numero entre 1 y 10: "))
    print("Numero romano: ", calcularromano(decimal))

main()