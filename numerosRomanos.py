#AUTOR: JOSÉ HEINZ MÖLLER SANTOS
#Este programa cambia de numeros normales a numeros romanos del 1 al 10.
#Para hacer numero de decimal a romano se hace:
def convertirANumeroRomano(numeroDecimal):
    #1 y 2 y 3 :
    if numeroDecimal>=1 and numeroDecimal<=3:
     return("I"*numeroDecimal)
    # 4:
    elif numeroDecimal==4:
     return("IV")
    #5:
    elif numeroDecimal==5:
     return("V")
    #6, 7 y 8:
    elif numeroDecimal>=6 and numeroDecimal<=8:
     return("V" + ("I" * (numeroDecimal-5)))
    #9:
    elif numeroDecimal == 9 :
     return("IX")
    #10:
    elif numeroDecimal==10:
     return("X")

def main():
    numeroDecimal= int(input("El número que hacer o convertir a romano: "))
    if numeroDecimal >= 1 and numeroDecimal <= 10:
        romano=convertirANumeroRomano(numeroDecimal)
        print("Tu número en Romano es:",romano)
    else:
        print("Pon entre el 1 Y  10")
main()

