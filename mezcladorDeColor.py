#encoding: UTF-8
#Raul Ortiz Mateos
#escribir un programa en donde el usuario ponga dos de los 3 colores primarios
#y le aparesca su color resultante pero si tecleas con todas mayusculas te sale error
# y para eso debes de empezar con una mayuscula

def combinarColores(c1,c2):

    if c1=="Rojo" and c2=="Azul" or c1=="Azul" and c2=="Rojo" :
         combinacion=("MORADO")
         return combinacion


    elif c1== "Rojo" and c2 == "Amarillo" or c1=="Amarillo" and c2=="Rojo":
         combinacion = ("Naranja")
         return combinacion

    elif c1 == "Azul" and c2 == "Amarillo" or c1=="Amarillo" and c2=="Azul":
        combinacion = ("VERDE")
        return combinacion

    elif c1=="Rojo" and c2=="Rojo":
        combinacion=("Rojo")
        return combinacion

    elif c1=="Azul" and c2=="Azul":
        combinacion=("Azul")
        return combinacion

    elif c1=="Amarillo" and c2=="Amarillo":
        combinacion=("Amarillo")
        return combinacion

def main():
    c1=str(input("Escribe el primer color:"))
    c2=str(input("Escribe el segundo color:"))
    color1 = c1.upper()
    color2= c2.lower()

    if color1==("Rojo") or c1==("Azul") or c1==("Amarillo"):
        print("El color es valido")
        combinar=combinarColores(c1,c2)
        print("El color combinado es:",combinar)
    elif color2==("rojo") or("azul")or ("amarillo"):
        print("solo se puede escribir con mayusculas la primera letra")


main()
