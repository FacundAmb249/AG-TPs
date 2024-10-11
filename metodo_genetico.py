import random

#Funcion que transforma binario a decimal
def bin_to_dec(cromosoma):
    dec = 0
    for i in range(len(cromosoma)):
        dec += cromosoma[i]*2**(len(cromosoma)-1-i) 
    return dec

#Funcion que crea la poblacion inicial en base a la cantidad de poblacion inicial y cantidad de genes que van a tener los cromosomas
def crear_poblacion(cant_poblacion, cant_genes):
    for _ in range(cant_poblacion):
        cromosoma = list(range(num_capitales))
        random.shuffle(cromosoma)  # Mezcla para crear una nueva permutación
        poblacion.append(cromosoma)
    return poblacion

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

def crossover_ciclico(padre1, padre2):
    length = len(padre1)
    hijo1 = [None] * length
    hijo2 = [None] * length
    visitado1 = [False] * length  #Índices visitados
    visitado2 = [False] * length

    #Elige de un índice inicial aleatorio
    indice_uno = random.randint(0, length - 1)

    indice_actual1 = indice_uno
    while not visitado[indice_actual1]:
        hijo1[indice_actual1] = padre1[indice_actual1]
        visitado1[indice_actual1] = True
        indice_actual1 = padre2.index(padre1[indice_actual1])

    indice_actual2 = indice_uno
    while not visitado[indice_actual2]:
        hijo2[indice_actual2] = padre2[indice_actual2]
        visitado2[indice_actual2] = True
        indice_actual2 = padre1.index(padre2[indice_actual2])

    for i in range(length):
        if hijo1[i] is None:
            hijo1[i] = padre2[i]
        if hijo2[i] is None:
            hijo2[i] = padre1[i]

    return hijo1, hijo2

#Funcion que calcula el fitness de cada uno de los cromosomas de la poblacion, en este caso el fitness es igual a la funcion objetivo
def fitness(poblacion):
    valores_funcion = []
    valores = []
    #Guardo los valores de los cromosomas en decimal y funcion objetivo de la poblacion
    for cromosoma in poblacion:
        valores.append(bin_to_dec(cromosoma))
        valores_funcion.append((bin_to_dec(cromosoma)/(2**30-1))**2)
    
    #Calcula el fitness de cada una de los cromosomas de la poblacion
    for i in range(cant_poblacion):
        fitnessPoblacion.append(valores_funcion[i]/sum(valores_funcion))
    return fitnessPoblacion

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

def generar_nueva_poblacion(poblacion, fitnessPoblacion):
    poblacion2 = []
    for i in range(recorrido):
        hijo1, hijo2 = crossover(padre1, padre2)
        hijo1 = mutacion(hijo1)
        hijo2 = mutacion(hijo2)
        poblacion2.append(hijo1)
        poblacion2.append(hijo2)
    return poblacion2

def metodo_genetico(distancias, ciudades, indice_ciudad):
    #Variables
    cant_poblacion = 50 #N = 50 Número de cromosomas de las poblaciones.
    cant_genes = len(bin(24))-2 #-2 para quitarle el 0b al principio
    probabilidad_crossover = 0 #A criterio
    probabilidad_mutacion = 0 #A criterio
    maxiteraciones = 200 #M = 200 Cantidad de ciclos.
    num_capitales = 23
    ciudad_inicial = ciudades[indice_ciudad]
    ciudades.pop(indice_ciudad)
    for i in range(len(distancias)):
        distancias[i].pop(indice_ciudad)

    #Pasar la distancia desde la capital elegida a las otras (una fila de la matriz)

    #Cromosomas: permutaciones de 23 números naturales del 1 al 23 donde cada gen es una ciudad.

    poblacion = []
    cromosoma = []

    #Creacion de la poblacion
    crear_poblacion(cant_poblacion, cant_genes)

    #iteraciones
    for iteraciones in range(maxiteraciones):
        fitnessPoblacion = []
        fitnessPoblacion = fitness(poblacion)
        poblacion = generar_nueva_poblacion(poblacion, fitnessPoblacion)
