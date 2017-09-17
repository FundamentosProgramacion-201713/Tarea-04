#encoding: UTF-8
#Gerardo Arturo Valderrama Quiroz
#A01374994
#Programa que recibe del 1 al 10 números e imprime su equivalente romano

#Funcion que detemina que numero romano le corresponde al numero dado y lo regresa
def determinarNumeroRomano(numero):
    if numero >=1 and numero <=3:
        romano = ("I" * numero)
        return romano
    elif numero == 4:
        romano = "IV"
        return romano
    elif numero >=5 and numero <=8:
        romano = ("V" +("I"*(numero%5)))
        return romano
    else:
        romano = (("I"*(9//numero))+"X")
        return romano

#Funcion principal main que lee, procesa e imprime datos
def main():
    numero = int(input("Teclea un número del 1 al 10: "))
    if numero >=1 and numero <=10:
        romano = determinarNumeroRomano(numero)
        print(" Su equivalente romano es", romano)
    else:
        print("ERROR: El número que dio no está entre el 1 y el 10")

main()