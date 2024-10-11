import random

#Funcion que transforma binario a decimal
def bin_to_dec(cromosoma):
    dec = 0
    for i in range(len(cromosoma)):
        dec += cromosoma[i]*2**(len(cromosoma)-1-i) 
    return dec

#Funcion que realiza la mutacion de un cromosoma mediante la inversion de un segmento del cromosoma
#Mutación de tipo inversa (Intro a AG cont, p. 13)
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

def crossover_ciclico(padre1, padre2):
    #(Intro a AG cont, p. 6)
    length = len(padre1)
    hijo = [None] * length
    visitado = [False] * length  #Índices visitados

    #Elige de un índice inicial aleatorio
    indice_uno = random.randint(0, length - 1)

    indice_actual = indice_uno
    while not visitado[indice_actual]:
        hijo[indice_actual] = padre1[indice_actual]
        visitado[indice_actual] = True

        indice_actual = padre2.index(padre1[indice_actual])

    for i in range(length):
        if hijo[i] is None:
            hijo[i] = padre2[i]

    return hijo

#Funcion que selecciona un cromosoma de la poblacion mediante el metodo del torneo
def torneo(fitnessPoblacion,poblacion):
    global cant_poblacion
    cromosomas_seleccionados = []
    max = []
    for i in range(4):
        cromosomas_seleccionados.append(poblacion[random.randint(0,cant_poblacion-1)])
    for i in range(4):
        if max == [] or fitnessPoblacion[poblacion.index(cromosomas_seleccionados[i])] > fitnessPoblacion[poblacion.index(max)]:
            max = cromosomas_seleccionados[i]
    return max

#main
#Variables
cant_poblacion = 50 #N = 50 Número de cromosomas de las poblaciones.
cant_genes = len(bin(2**30-1))-2 #-2 para quitarle el 0b al principio
probabilidad_crossover = 0
probabilidad_mutacion = 0
maxiteraciones = 200 #M = 200 Cantidad de ciclos.

#pasar la distancia desde la capital elegida a las otras (una fila de la matriz)

#Cromosomas: permutaciones de 23 números naturales del 1 al 23 donde cada gen es una ciudad.

poblacion = []
cromosoma = []