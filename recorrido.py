#Ejercicio 7

lista=[18,50,210,80,145,333,70,30]

def sacar_multiplos10_menor100(lista):
    for elements in lista:
        if elements>300:
            break
        else:
            if elements%10==0 and elements<200:
                print(elements)

if __name__=="__main__":
    sacar_multiplos10_menor100(lista)

