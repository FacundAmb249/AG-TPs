import sys
import random
from distancias import cargar_distancias

c,d = cargar_distancias()

#Funcion que crea la poblacion inicial en base a la cantidad de poblacion inicial y cantidad de genes que van a tener los cromosomas

def crear_poblacion(cant_poblacion, cant_genes):
    cromosoma = list(range(cant_genes))
    poblacion = [] * cant_poblacion
    for i in range(cant_poblacion):
        random.shuffle(cromosoma)
        temp = cromosoma.copy()
        if temp not in poblacion: 
            poblacion.append(temp)
        else: 
            i = i - 1
    return poblacion

def calcular_distancias(cant_poblacion, cant_genes, poblacion, distancias):
    distancia_recorrido = [0] * cant_poblacion
    for i in range(cant_poblacion):
        dist = 0
        lista = poblacion[i]
        for j in range(cant_genes - 1):
            dist = dist + distancias[lista[j]][lista[j+1]]
        distancia_recorrido[i] = dist
    return distancia_recorrido 

def fitness(cant_poblacion, distancias):
    fitness = [0] * cant_poblacion
    for i in range(cant_poblacion):
        fitness[i] = (1 / distancias[i]) 
    sumatoria_fitness = sum(fitness)
    fitness_normalizado = [fit/sumatoria_fitness for fit in fitness]
    print(sum(fitness_normalizado))
    return fitness_normalizado


#Funcion que realiza el crossover entre dos cromosomas mediante el metodo de un punto de corte
def crossover_ciclico(padre1, padre2, probabilidad_crossover):
    randomNumCross = random.random()
    if randomNumCross < probabilidad_crossover:
        #Se asume que ambos padres tienen las mismas dimensiones
        hijo1 = [-1] * len(padre1)
        hijo2 = [-1] * len(padre2)

        #Asigno los primeros valores de los hijos y agrego una variable para determinar el último valor encontrado
        hijo1[0] = padre1[0]
        hijo2[0] = padre2[0]
        ultimo_encontrado = padre2[0]
        length = 0

        while length < len(padre1):
            if ultimo_encontrado == padre1[0]:
                #termina
                for i in range(len(padre1)):
                    if hijo1[i] == -1:
                        hijo1[i] = padre2[i]
                    if hijo2[i] == -1:
                        hijo2[i] = padre1[i]
                length = len(padre1)
            else:
                indice = padre1.index(ultimo_encontrado)
                hijo1[indice] = padre1[indice]
                hijo2[indice] = padre2[indice]
                ultimo_encontrado = padre2[indice]
                length += 1
    else:
        hijo1 = padre1
        hijo2 = padre2

    return hijo1, hijo2

#Funcion que realiza la mutacion de un cromosoma, inverte dos cromosomas random de lugar
def mutacion(hijo, probabilidad_mutacion):
    randomNumMut = random.random()
    if randomNumMut < probabilidad_mutacion: 
        index = random.sample(hijo,2)
        hijo[index[0]], hijo[index[1]] = hijo[index[1]], hijo[index[0]]
    return hijo

#Funcion que selecciona un cromosoma de la poblacion mediante el metodo de la ruleta
def ruleta(fitness_recorrido, poblacion):
    return random.choices(poblacion, weights = fitness_recorrido, k = 1)[0]
    # acum1 = 0
    # acum2 = 0
    # indiceCromosoma = 0
    # for i in range(len(fitness_poblacion)):
    #     acum1 += fitness_poblacion[i]
    # randomNum = random.uniform(0, acum1)
    # for i in range(len(fitness_poblacion)):
    #     if randomNum > acum2:
    #         indiceCromosoma += 1
    #         acum2 += fitness_poblacion[i]
    # if indiceCromosoma == len(fitness_poblacion):
    #     indiceCromosoma = len(fitness_poblacion) - 1
    # return poblacion[indiceCromosoma]

#Funcion que selecciona los dos cromosomas/20% con mayor valor de la poblacion
def elitismo(poblacion, fitness_poblacion):
    #Obtengo los dos cromosomas con mayor valor
    fitness_acomodado = sorted(fitness_poblacion,reverse=True)
    maximos = fitness_acomodado[:2]
    cromosomas = []
    for i in range(2):
        indice = fitness_poblacion.index(maximos[i])
        cromosomas.append(poblacion[indice])
    cromosoma1 = cromosomas[0]
    cromosoma2 = cromosomas[1]
    return cromosoma1, cromosoma2

#Funcion que genera una nueva poblacion en base a la poblacion anterior y sus fitness aplicando o no elitismo y ruleta o torneo
def generar_nueva_poblacion(poblacion, fitness_recorrido,probabilidad_mutacion, probabilidad_crossover, boolElitismo):
    global cant_poblacion
    poblacion2 = []
    e = 0

    if boolElitismo:
        cromosoma1, cromosoma2 = elitismo(poblacion, fitness_recorrido)
        poblacion2.append(cromosoma1)
        poblacion2.append(cromosoma2)
        e = 1

    for i in range(0, len(poblacion) - e, 2):
        padre1 = ruleta(fitness_recorrido, poblacion)
        padre2 = ruleta(fitness_recorrido, poblacion)
        while padre1 == padre2:
            padre2 = ruleta(fitness_recorrido, poblacion)
        hijo1, hijo2 = crossover_ciclico(padre1, padre2, probabilidad_crossover)
        hijo1 = mutacion(hijo1, probabilidad_mutacion) 
        hijo2 = mutacion(hijo2, probabilidad_mutacion) 
        poblacion2.append(hijo1)
        poblacion2.append(hijo2)

    return poblacion2

def metodo_genetico(distancias, boolElitismo):
    #VARIABLE INICIALES
    cant_poblacion = 50
    cant_genes = 24
    probabilidad_crossover = 0.7
    probabilidad_mutacion = 0.2
    maxiteraciones = 1500

    distancia_menor = 0

    poblacion = crear_poblacion(cant_poblacion, cant_genes)
    distancia_recorrido = calcular_distancias(cant_poblacion, cant_genes, poblacion, distancias)
    fitness_recorrido = fitness(cant_poblacion, distancia_recorrido)

    for i in range(maxiteraciones):
        print("iteracion:", i + 1)
        poblacion = generar_nueva_poblacion(poblacion, fitness_recorrido,probabilidad_mutacion, probabilidad_crossover, boolElitismo)
        # print("Poblacion nueva",poblacion)
        # print("Tamanio poblacion",len(poblacion))
        # print("Fitness",fitness_recorrido)

        distancia_recorrido = calcular_distancias(cant_poblacion, cant_genes, poblacion, distancias)
        fitness_recorrido = fitness(cant_poblacion, distancia_recorrido)

        # temp_min_d = min(distancia_recorrido)
        # temp_min_i = distancia_recorrido.index(temp_min_d)
        #
        # if (i == 0) or (temp_min_d < distancia_menor):
        #     distancia_menor = temp_min_d
        #     distancia_menor_i = temp_min_i
        #     recorrido = poblacion[distancia_menor_i]
        # print("actual:", temp_min_d, temp_min_i)
        # print("mejor:", distancia_menor, distancia_menor_i)
        # print("recorrido:", recorrido)

    print(poblacion)
        
    return recorrido, distancia_menor

metodo_genetico(d, False)
