#Ejercicio 4

lista=["mundo",2,True,2.4]

def dos_elem_fin_list(list):
    nueva_lista=list[::-1]
    lista=nueva_lista[0:-1:2]
    return lista 

def cambiar_pos(lista):
    elem1=lista[0]
    elem2=lista[-1]
    nueva_lista=lista
    nueva_lista[0]=elem2
    nueva_lista[-1]=elem1
    return nueva_lista

def eliminar(lista):
    elem=lista[-1]
    lista.remove(elem)
    return lista

def list_dupe_elem(lista):
    elem=lista[1]
    lista.append(elem)
    return lista

print(lista)
print(dos_elem_fin_list(lista))
print(cambiar_pos(lista))
lista_nueva=cambiar_pos(lista)
print(eliminar(lista_nueva))
lista2=eliminar(lista_nueva)
print(list_dupe_elem(lista2))