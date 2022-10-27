#Ejercicio 5

import sys


def pedir_num():
    numero=input("Introduce un número entero positivo: ")
    try:
        numero=int(numero)
    except:
        print("Se ha de introducir un número entero positivo",file=sys.stderr())
        sys.exit
    return numero

pedir_num()

def lista_num(num):
    numero=str(num)
    lista_num=numero.split()
    return lista_num