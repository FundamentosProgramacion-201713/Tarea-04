#encoding: UTF-8
#sebastian Morales Martin
#define el resultante de la mezcla de los colores
a = "amarillo"
r = "rojo"
az = "azul"
def main(): #compila los datos de los colores, llama a la funcion para combinarlos y las resuelve
    color1 = input("Ingrese el primer color (rojo, azul, amarillo): ")
    color2 = input("Ingrese el segundo color (rojo, azul, amarillo): ")
    if color1 and color2 != a and r and az:
        print("ERROR")
    mezcla = encontrarMezcla(color1, color2)
    print(mezcla)

def encontrarMezcla(color1, color2): #encuentra la mezcla entre los dos colores
    if color1 == a and color2 == r:
        mezcla = "Naranja"
        return mezcla
    elif color1 == r and color2 == az:
        mezcla = "Morado"
        return mezcla
    elif color1 == az and color2 == a:
        mezcla = "Verde"
        return mezcla

main()