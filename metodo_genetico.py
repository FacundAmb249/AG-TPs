#pasar la distancia desde la capital elegida a las otras (una fila de la matriz)

#N = 50 Número de cromosomas de las poblaciones.
#M = 200 Cantidad de ciclos.
#Cromosomas: permutaciones de 23 números naturales del 1 al 23 donde cada gen es una ciudad.
#Crossover cíclico. (Intro a AG cont, p. 6)
#Mutación binaria (?) (Intro a AG cont, p. 14)

import random

#Funcion que transforma binario a decimal
def bin_to_dec(cromosoma):
    dec = 0
    for i in range(len(cromosoma)):
        dec += cromosoma[i]*2**(len(cromosoma)-1-i) 
    return dec

#Funcion que realiza la mutacion de un cromosoma mediante la inversion de un segmento del cromosoma
#Mutación de tipo inversa
def mutacion (hijo): 
    num = random.randrange(0,100)
    if num < (probabilidad_mutacion*100):
        punto1 = random.randint(0,cant_genes-1)
        punto2 = random.randint(0,cant_genes-1)
        #si los puntos son iguales o consecutivos se vuelve a buscar, ya que sino el cromosoma queda igual
        while punto1 == punto2 or abs(punto1 - punto2) == 1:
            punto1 = random.randint(0, len(hijo) - 1)
            punto2 = random.randint(0, len(hijo) - 1)
        if punto1 > punto2:
            punto1, punto2 = punto2, punto1
        hijo = hijo[:punto1] + hijo[punto1:punto2][::-1] + hijo[punto2:]
    return hijo
