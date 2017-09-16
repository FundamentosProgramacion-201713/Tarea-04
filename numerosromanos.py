#UTF-8
#Autor: Nazdira Abigail Cerda del Prado A01375428
#Convierte de decimal a romano

#Esta función convierte de decimal a romanos
def convertirRomanos(numdecimal):
    if(numdecimal==1 or numdecimal==2 or numdecimal==3): #Para 1,2,3
        return ("I"*numdecimal)
    elif(numdecimal==4): #Para 4
        return "IV"
    elif(numdecimal==5): #Para 5
        return "V"
    elif (numdecimal==6 or numdecimal==7 or numdecimal==8): #Para 6,7,8
        return("V"+"I"*(numdecimal-5))
    elif(numdecimal==9):#Para 9
        return "IX"
    elif(numdecimal==10): #Para 10
        return "X"
def main():
    numdecimal=int(input("Ingrese número entero entre 1 y 10:"))
    if (numdecimal>0 and numdecimal<=10):
        numromano=(convertirRomanos(numdecimal))
        print("El número", numdecimal, "corresponde al número", numromano, "en romano.")
    else:
        print("ERROR, ingrese un número entre el 1 y el 10")

main()