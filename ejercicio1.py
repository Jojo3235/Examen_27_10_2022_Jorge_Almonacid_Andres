#Ejercicio 1

def minusc(string):
    return string.lower()
    
def caps(string):
    return string.upper()

var_1= "Módulo 1 de Python"

print(minusc(var_1))
print(caps(var_1))

def longitud(string):
    return len(string)

print(longitud(var_1))

def div(length,num):
    return "{:.04}".format(int(length)/int(num))
longitud_var=longitud(var_1)

print(div(longitud_var,7))

def funcion1():
    return (12-(4*2)-(2+2))

print(funcion1())

def funcion2():
    return 12-4*(2-2)+2

print(funcion2())

def funcion3():
    edad = int(input("Introduce tu edad: "))
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")

funcion3()