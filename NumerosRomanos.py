#enconding: UTF-8
#Alejandro Chávez Campos, A01374974
#Este programa es para mostrar un el número romano que corresponde a un número dado por el usuario.

def calcularRomano(numero): #Determina el número romano a partir del número
    if numero>=1 and numero<=3 :
        romano= numero*"I"
        return romano
    elif numero >=4 and numero <=5 :
        romano =(5-numero)*"I"
        strRomano =("{}V".format(romano))
        return strRomano
    elif numero>5 and numero<=8 :
        romano= (numero-5)*"I"
        strRomano= ("V{}".format(romano))
        return strRomano
    elif numero >= 9 and numero <=10 :
        romano=(10-numero)*"I"
        strRomano = ("{}X".format(romano))
        return strRomano

def main(): #Programa principal
    numero=int(input("Dame el número :"))

    if numero >=1 and numero<=10:
        strRomano = calcularRomano(numero)
        print("El número {} equivale a {} ".format(numero, strRomano))

    else:
        print ("Error")

main()