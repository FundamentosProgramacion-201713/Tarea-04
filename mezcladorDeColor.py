#encoding: UTF-8
#Raul Ortiz Mateos
#escribir un programa en donde el usuario ponga dos de los 3 colores primarios
#y le aparesca su color resultante pero si tecleas con todas mayusculas te sale error
# y para eso debes de empezar con una mayuscula

def combinarColores(c1,c2):
    if c1=="Rojo"  and c2=="Azul" or c1=="Azul"  and c2=="rojo":
        return ("Morado")
    elif c1=="Rojo" and c2=="Amarillo":
        return ("naranja")
    elif c1== "Rojo" and c2=="Rojo":
        return("Rojo")


