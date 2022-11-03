#Ejercicio 6

def borrar_duplicados(lista_num):
    lista=list(set(lista_num))
    return lista

def ordenar(lista_num):
    lista_num.sort()
    return lista_num

def eliminar_impares(lista_num):
    for elements in lista_num:
        if elements%2==1:
            lista_num.remove(elements)
            return lista_num

def suma_num(lista_num):
    return sum(lista_num)

def añadir_sum(lista_num):
    lista_num[::-1]
    suma=suma_num(lista_num)
    lista_num.append(suma)
    lista=lista_num[::-1]
    return lista

def modificar(lista_num):
    lista_num1=borrar_duplicados(lista_num)
    lista_num2=ordenar(lista_num1)
    lista_num3=eliminar_impares(lista_num2)
    lista_num4=añadir_sum(lista_num3)
    return lista_num4

def comprobar(lista_num):
    lista=modificar(lista_num)
    print(lista[0]==sum(lista[1:]))

lista=[3,2,3,4,41,3,3,4,3]

if __name__=="__main__": 
    print(modificar(lista))
    comprobar(lista)
