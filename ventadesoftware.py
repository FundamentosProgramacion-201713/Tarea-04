#Autor: Mónica Monserrat Palacios Rodríguez
#UTF-8
#Calcular el precio total por paquetes comprados.

def calcularPrecio(cantidad):#Se caclcula el precio por los pauetes asignados independientemente del descuento
    total=cantidad*1500
    return total

def calcularDescuento(cantidad):#Se calcula el descuento total dependiendo de as condiciones establecidas
    total1=calcularPrecio(cantidad)
    if cantidad>=0 and cantidad <=9:
        return total1

    elif cantidad>=10 and cantidad <=19:
        total2=total1-(total1*.20)
        return total2

    elif cantidad >= 20 and cantidad <= 49:
        total2 = total1 - (total1 * .30)
        return total2

    elif cantidad >= 50 and cantidad <= 99:
        total2 = total1 - (total1 * .40)
        return total2

    elif cantidad >= 100:
        total2 = total1 - (total1 * .50)
        return total2

def main():#Función principal donde se leen e imrpimen los valores

    cantidad=int(input("Teclee la cantidad de paquetes comprados: "))
    if cantidad>=0:
        total1=calcularDescuento(cantidad)#Se llama a la función
        print ("El costo total de los paquetes con el desceunto incluido es de: $",total1)
    else:
        print("ERROR, sólo números positivos por favor")

main()#Se llama a la función main.