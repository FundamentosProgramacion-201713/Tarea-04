# encoding: UTF:8
# Raul Ortiz Mateos A01375407
# leer un programa que lea del numero 1 a l 10 en numeros romanos y si sale arriba de diez
# que salga un mensaje que salga error.



def pasarANumerosRomanos(n):
    if 1<=n and n<= 3:
        numeroRomano = (n*"I")

        return numeroRomano


    elif n == 4:
        numeroRomano=("I"+"V")

        return numeroRomano

    elif 5<=n and n<=8:
        numeroRomano= ("V"+(n-5)*"I")
        return numeroRomano

    elif n == 9:
        numeroRomano= ((n%2)*"I"+"X")
        return numeroRomano

    elif n==10:
        numeroRomano=  ((n % 2)*"I"+"X")
        return numeroRomano

def main():
    n = int(input("¿que numero quieres pasar a romano? "))
    numero = int(n)
    if numero == n and numero >= 1 and numero <= 10:

        numeroR = (pasarANumerosRomanos(n))

        print("El numero que elegiste, en romano se representa como:",numeroR)
    else:
        print("error, Solo puedes elegir entre  el numero 1 y el 10")

main()









