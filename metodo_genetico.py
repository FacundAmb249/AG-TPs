import sys
import random
#Funciones obsoletas: generar_nueva_poblacion

#VARIABLE INICIALES
cant_poblacion = 50
cant_genes = 24
probabilidad_crossover = 0.7
probabilidad_mutacion = 0.2
maxiteraciones = 200

poblacion = []
cromosoma = []

distancia_recorrido = [0] * cant_poblacion
fitness_poblacion = [0] * cant_poblacion
datos_valores = []
datos_poblacionales = []
maxCromosoma = []

#Funcion que crea la poblacion inicial en base a la cantidad de poblacion inicial 
#y cantidad de genes que van a tener los cromosomas

def crear_poblacion(cant_poblacion, cant_genes):
    for _ in range(cant_poblacion):
        cromosoma = [random.randint(0, 1) for i in range(cant_genes)]
        poblacion.append(cromosoma)
    return poblacion

def calcular_distancias(cant_poblacion, cant_genes, distancias):
    for i in range(cant_poblacion):
        dist = 0
        for j in range(cant_genes):
            dist = dist + distancias[poblacion[i][j]][poblacion[i][j + 1]]
        distancia_recorrido[i] = dist
        fitness_poblacion[i] = 1 / dist
    return distancia_recorrido

#Funcion que realiza el crossover entre dos cromosomas mediante el metodo de un punto de corte
def crossover_ciclico (padre1, padre2):
    num = random.randrange(0,100)
    if num > (probabilidad_crossover*100):
        hijo1 = padre1
        hijo2 = padre2
    else:
        hijo1 = [-1] * len(padre2)
        hijo2 = [-1] * len(padre2)

        #Asigno los primeros valores de los hijos 
        hijo1[0] = padre1[0]
        hijo2[0] = padre2[0]

        index = 0
        while padre2[index] not in hijo1: 
            index = padre1.index(padre2[index])
            hijo1[index] = padre1[index]

        index2 = 0
        while padre1[index2] not in hijo2:
            hijo2[index2] = padre2[index2]
            index2 = padre2.index(padre1[index2])

        for i in range(len(padre1)):
            if hijo1[i] == -1:
                hijo1[i] = padre2[i]
            if hijo2[i] == -1:
                hijo2[i] = padre1[i]


    return hijo1, hijo2

#Funcion que realiza la mutacion de un cromosoma, inverte dos cromosomas random de lugar
def mutacion (hijo): 
    index = random.sample(hijo,2)
    hijo[index[0]], hijo[index[1]] = hijo[index[1]], hijo[index[0]]
    return hijo

#Calcula el recorrido más fit (fittest) en cada generación
#Busca el valor más bajo de distancia_recorrido y devuelve su índice
def fittest(cant_poblacion, distancia_recorrido):
    minimo = min(distancia_recorrido)
    min_indice = distancia_recorrido.index(minimo)
    return min_indice

#Funcion que selecciona un cromosoma de la poblacion mediante el metodo de la ruleta
def ruleta(fitness_poblacion, poblacion):
    randomNum = random.random()
    acum = 0
    indiceCromosoma = 0
    for i in range(len(fitness_poblacion)):
        if randomNum > acum and randomNum < (acum + fitness_poblacion[i]):
            indiceCromosoma = i
            break  
        acum += fitness_poblacion[i]
    return poblacion[indiceCromosoma]

#Funcion que selecciona los dos cromosomas/20% con mayor valor de la poblacion
def elitismo(poblacion,fitness_poblacion):
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
def generar_nueva_poblacion(poblacion, fitness_poblacion, boolElitismo):
    global cant_poblacion
    poblacion2= []
    recorrido = (cant_poblacion//2)
    if boolElitismo == True:
        cromosoma1, cromosoma2 = elitismo(poblacion, fitness_poblacion)
        poblacion2.append(cromosoma1)
        poblacion2.append(cromosoma2)
        recorrido = ((cant_poblacion//2) -1)
    for i in range(recorrido):
        padre1 = ruleta(fitness_poblacion,poblacion)
        padre2 = ruleta(fitness_poblacion,poblacion)
        hijo1, hijo2 = crossover_ciclico(padre1, padre2)
        hijo1 = mutacion(hijo1)
        hijo2 = mutacion(hijo2)
        poblacion2.append(hijo1)
        poblacion2.append(hijo2)
    return poblacion2

def metodo_genetico(distancias, ciudades, boolElitismo):
    if boolElitismo == True:
        print("elitismo")
    print("hallo")

padre1 = [9,8,2,1,7,4,5,10,6,3]
padre2 = [1,2,3,4,5,6,7,8,9,10]
hijo1,hijo2 = crossover_ciclico(padre1,padre2)
print("hijo1",hijo1)
print("hijo2",hijo2)


# #Creacion de la poblacion
# crear_poblacion(cant_poblacion, cant_genes)
#
# #iteraciones
# for iteraciones in range(maxiteraciones):
#     fitness_poblacion = []
#     fitness_poblacion = fitness(poblacion)
#     poblacion = generar_nueva_poblacion(poblacion, fitness_poblacion, boolElitismo, boolRuleta)
#
#
# print("cromosoma con mejor distancia:")
# print(maxCromosoma)

