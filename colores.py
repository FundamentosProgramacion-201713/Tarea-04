#Encoding: UTF-8
#Autor: Angel Roberto Pesado Bartolo A01374942
#Descripcion: Pedir al usuario 2 colores de la lista señalada e imprimir su combinación de esos dos colores.

def mezclarColores(colorm1,colorm2): #Definir la función que indique que color se formará
    if colorm1 == "azul" and colorm2 == "azul": #Si ambos colores son azul, se regresará el color azul
        return("Azul")
    elif colorm1 == "amarillo" and colorm2 == "amarillo": #Si ambos colores son amarillo, se regresará el color amarillo
        return("Amarillo")
    elif colorm1 == "rojo" and colorm2 == "rojo": #Si ambos colores son rojo, se regresará el color rojo
        return("Rojo")
    elif (colorm1 == "rojo" and colorm2 == "azul") or (colorm1 == "azul" and colorm2 == "rojo"): #Si los colores son rojo y azul , el programa regresa el color Mordado
        return("Morado")
    elif (colorm1 == "rojo" and colorm2 == "amarillo") or (colorm1 == "amarillo" and colorm2 == "rojo"): #Si los colores son rojo y amarillo, el programa regresa el color Naranja
        return("Naranja")
    elif (colorm1 == "azul" and colorm2 == "amarillo") or (colorm1 == "amarillo" and colorm2 == "azul"): #Si los colores son azul y amarillo, el programa regresa el color Verde
        return("Verde")
    else:
        return("Los colores que ingresaste no son validos") #Si no se ingresan los colores mencionados, regresará el mensaje

def main():
    print("Los colores que tienes disponibles son: Azul,Rojo y Amarillo") #Imprimimos que colores están disponibles
    color1 = input("Ingrese el primer color: ")  # Pedimos al usuario el primer color
    color2 = input("Ingrese el segundo color: ") #Pedimos al usuario el segundo color
    colorm1 = color1.lower()       #.lower cambia a minuscula los datos ingresados por el usuario
    colorm2 = color2.lower()
    print("Si se mezcla  " , colorm1, "y" , colorm2 , "obtendra: ", mezclarColores(colorm1,colorm2)) #Imprimimos que  color se forma a partir de mandar los datos dados por el usuario a la función mezclarColores
main()           #Llamamos a la funcion main para que realice lo que  tiene dentro de ella
