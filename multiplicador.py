#Ejercicio 3

numero_magico=12345679

def pedir_numero():
    numero=int(input("Introduzca un número entre 1 y 9: "))
    return numero

def multiplicar_9(num):
    numero=9*num
    print(num,"*","9=",numero)

numero_pedido=pedir_numero()
multiplicar_9(numero_pedido)

def multiplicación_mágica(num):
    numero=num*numero_magico
    print(num,"*",numero_magico,"=",numero)

multiplicación_mágica(numero_pedido)
