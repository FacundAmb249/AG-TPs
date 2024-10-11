import random

#Funcion que crea la poblacion inicial en base a la cantidad de poblacion inicial y cantidad de genes que van a tener los cromosomas
def crear_poblacion(cant_poblacion, num_capitales):
    for _ in range(cant_poblacion):
        cromosoma = list(range(num_capitales))
        random.shuffle(cromosoma) #Mezcla para crear una nueva permutación
        poblacion.append(cromosoma)
    return poblacion

#Funcion que realiza la mutacion de un cromosoma mediante la inversion de un segmento del cromosoma
#Mutación binaria de un bit
def mutacion(hijo):
    num = random.randrange(0,100)
    if num < (probabilidad_mutacion*100):
        punto_m = random.randint(0,num_capitales-1)
        hijo_lista = list(hijo) #Convierte a lista para facilitar modificación
        punto2 = random.randint(0,num_capitales-1)
        hijo_lista[punto_m], hijo_lista[punto2] = hijo_lista[punto2], hijo_lista[punto_m]
        hijo[punto_m] = random.randint(0, num_capitales - 1) #Vuelve a convertir a cadena
    return hijo

def crossover_ciclico(padre1, padre2):
    num = random.randrange(0,100)
    print("padre1:", padre1)
    print("padre2:", padre2)
    if num > (probabilidad_crossover*100):
        hijo1 = padre1
        hijo2 = padre2
    else:
        length = len(padre1)
        hijo1 = [None] * length
        hijo2 = [None] * length
        #Índices visitados
        visitado1 = [False] * length
        visitado2 = [False] * length

        #Elige de un índice inicial aleatorio
        indice_uno = random.randint(0, length - 1)

        indice_actual1 = indice_uno
        while not visitado1[indice_actual1]:
            hijo1[indice_actual1] = padre1[indice_actual1]
            visitado1[indice_actual1] = True
            indice_actual1 = padre2.index(padre1[indice_actual1])

        indice_actual2 = indice_uno
        while not visitado2[indice_actual2]:
            hijo2[indice_actual2] = padre2[indice_actual2]
            visitado2[indice_actual2] = True
            indice_actual2 = padre1.index(padre2[indice_actual2])

        for i in range(length):
            if hijo1[i] is None:
                hijo1[i] = padre2[i]
            if hijo2[i] is None:
                hijo2[i] = padre1[i]
    print("hijo1:", hijo1)
    print("hijo2:", hijo2)
    return hijo1, hijo2

#Funcion que calcula el fitness de cada uno de los cromosomas de la poblacion. Agrega las distancia recorrida a un arreglo
def fitness(poblacion, distancias):
    fitnessPoblacion = []
    for cromosoma in poblacion:
        distancia = calcular_distancia(cromosoma, distancias)
        fitnessPoblacion.append(distancia)
    return fitnessPoblacion

#Calcula distancia total del recorrido
def calcular_distancia(cromosoma, distancias):
    distancia_total = 0
    for i in range(len(cromosoma)):
        distancia_total += distancias[cromosoma[i]][cromosoma[(i + 1) % len(cromosoma)]]
    return distancia_total

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
    while len(poblacion2) < len(poblacion):
        padre1 = torneo(fitnessPoblacion,poblacion)
        padre2 = torneo(fitnessPoblacion,poblacion)
        hijo1, hijo2 = crossover_ciclico(padre1, padre2)
        hijo1 = mutacion(hijo1)
        hijo2 = mutacion(hijo2)
        poblacion2.append(hijo1)
        poblacion2.append(hijo2)
    return poblacion2

def metodo_genetico(distancias, ciudades):
    #Variables
    global probabilidad_crossover, probabilidad_mutacion, cant_poblacion, num_capitales, poblacion, cromosoma
    cant_poblacion = 50 #N = 50 Número de cromosomas de las poblaciones.
    probabilidad_crossover = 0.7 #A criterio
    probabilidad_mutacion = 0.2 #A criterio
    maxiteraciones = 200 #M = 200 Cantidad de ciclos.
    num_capitales = 24 #Cromosomas: permutaciones de 23 números naturales del 1 al 23 donde cada gen es una ciudad.

    #Pasar la distancia desde la capital elegida a las otras (una fila de la matriz)

    poblacion = []
    cromosoma = []

    #Creacion de la poblacion
    poblacion = crear_poblacion(cant_poblacion, num_capitales)

    #iteraciones
    for iteraciones in range(maxiteraciones):
        fitnessPoblacion = []
        fitnessPoblacion = fitness(poblacion, distancias)
        poblacion = generar_nueva_poblacion(poblacion, fitnessPoblacion)

    recorrido = min(poblacion, key=lambda cromosoma: calcular_distancia(cromosoma, distancias))
    distancia = calcular_distancia(recorrido, distancias)

    recorrido
    print(recorrido, distancia)
    return recorrido, distancia
