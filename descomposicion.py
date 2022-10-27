#Ejercicio 5

def pedir_num():
    numero=input("Introduce un número entero positivo: ")
    try:
        numero=int(numero)
    except:
        print("Se ha de introducir un número entero positivo")
    return numero

def listificar():
    numero=pedir_num()
    lista=list(str(numero))
    return lista

lista_numeros=listificar()
print(lista_numeros)