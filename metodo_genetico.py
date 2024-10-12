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

def fillNoneWithSwappedValue(arr1 ,arr2 ,final1 ,final2 ):
    for a in range(0,len(arr1)):
        if final1[a] == None:
            final1[a] = arr2[a]
        if final2[a] == None:
            final2[a] = arr1[a]
    return final1,final2

def indexOf(arr,x):
    for a in range(0,len(arr)):
        if arr[a] == x:
            return a
    return -1


def crossoverOperator( padre1, padre2 ):
    hijo1 = [None] * len(padre1)
    hijo2 = [None] * len(padre2)
    size1 = 1
    size2 = 1

    initalSelected = padre1[0]
    hijo1[0] = padre1[0]
    latestUpdated2 = padre2[0]
    check = 1

    while size1 < len(padre1) or size2 < len(padre2):
        if latestUpdated2 == initalSelected:
            index2 = indexOf(padre2,latestUpdated2)
            hijo2[index2] = padre2[index2]
            ans1,ans2 = fillNoneWithSwappedValue(padre1, padre2, hijo1, hijo2)
            hijo1 = ans1
            hijo2 = ans2
            size1 = len(padre1)
            size2 = len(padre2)
            check = 0
        else:
            index2 = indexOf(padre2,latestUpdated2)
            hijo2[index2] = padre2[index2]
            size2 += 1
            index1 = indexOf(padre1,padre2[index2])
            hijo1[index1] = padre1[index1]
            size1 += 1
            latestUpdated2 = padre2[index1]
    if check:
        index2 = indexOf(padre2, latestUpdated2)
        hijo2[index2] = padre2[index2]
    return hijo1,hijo2

def findUnusedIndexValues(parent,offspring):
    res = list()
    for a in parent:
        if indexOf(offspring,a) == -1:
            res.append(a)
    return res

def crossover_ciclico( padre1, padre2 ):
    print('hellol shakoob')
    hijo1 = [None] * len(padre1)
    hijo2 = [None] * len(padre2)
    i1 = 0
    i2 = -1
    initalSelected = padre1[0]
    hijo1[i1] = padre2[0]
    i1 += 1
    # latestUpdated2 = padre2[0]
    check = 1

    while i1 < len(padre1)-1 and i2 < len(padre2) -1:
        index1 = indexOf(padre1,hijo1[i1-1])
        index1 = indexOf(padre1,padre2[index1])
        latestUpdated2 = padre2[index1]
        if latestUpdated2 == initalSelected:
            hijo2[i2] = latestUpdated2
            i2 += 1
            # print("cycle detected")
            check = 0
            res1 = findUnusedIndexValues(padre1,hijo1)
            res2 = findUnusedIndexValues(padre2,hijo2)
            # print(res1,res2)
            ans1,ans2 = crossover_ciclico(res1, res2)
            hijo1[i1:] = ans1
            hijo2[i2:] = ans2
            check = 0
            break
        else:
            hijo2[i2] = padre2[index1]
            i2 += 1
            index1 = indexOf(padre1,hijo2[i2-1])
            hijo1[i1] = padre2[index1]
            i1 += 1
    if check:
        index1 = indexOf(padre1, hijo1[i1 - 1])
        index1 = indexOf(padre1, padre2[index1])
        latestUpdated2 = padre2[index1]
        hijo2[i2] = latestUpdated2
        i2 += 1
    return hijo1,hijo2

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
