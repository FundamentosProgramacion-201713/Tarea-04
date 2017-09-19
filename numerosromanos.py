#Encoding UTF-8
#Anaid Fernanda Labat González, A01746289
#Covertir de números decimales a números romanos

def calcularNumeroRomano(n):
    if n>=1 and n<=3:
        numeroRomano= (n*"I")
    elif n==4:
        numeroRomano="IV"
    elif n==5:
        numeroRomano="V"
    elif n==6:
        numeroRomano="VI"
    elif n==7:
        numeroRomano="VII"
    elif n==8:
        numeroRomano="VIII"
    elif n==9:
        numeroRomano= "IX"
    elif n==10:
        numeroRomano= "X"
    return numeroRomano

#Se define la función principal para imprimir la conversión o un error si el número no está entre  y 10
def main():
    noRomano=int(input("Ingresar un número entre 1 y 10:"))
    if noRomano>=1 and noRomano<=10:
        numeroRomano = calcularNumeroRomano(noRomano)
        print("El número romano es:", numeroRomano)
    else:
        print("ERROR, teclee un número entre 1 y 10")
main()




