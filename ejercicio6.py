#Ejercicio 6

def modificar(lista_num):
    lista=list(set(lista_num))
    lista.sort()
    for elements in lista:
        elements=int(elements)
        if elements%2==1:
            elements.remove(lista)
    suma=sum(lista)
    