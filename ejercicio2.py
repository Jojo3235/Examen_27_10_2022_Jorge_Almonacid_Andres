#Ejercicio 2

cadena="zeréP nauJ,01"
def voltear_cadena(cadena):
    cadena_arreglada=cadena[::-1]
    return cadena_arreglada

def listificar_cadena(cadena):
    cadena_arreglada=voltear_cadena(cadena)
    cadena_sep=cadena_arreglada.split(",")
    return cadena_sep

lista_cadena=listificar_cadena(cadena)
def resultado(lista):
    el1=lista[0]
    el2=lista[1]
    return "{} ha sacado un {} de nota".format(el2,el1)

if __name__=="__main__":
    print(resultado(lista_cadena))