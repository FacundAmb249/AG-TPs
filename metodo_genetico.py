import sys
import random
import matplotlib.pyplot as plt
import pandas as pd

#VARIABLE INICIALES
cant_poblacion = 50
ciclos = 200
cant_genes = 24
probabilidad_crossover = 0
probabilidad_mutacion = 0
maxiteraciones = 100

poblacion = []
cromosoma = []

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

#Funcion que realiza el crossover entre dos cromosomas mediante el metodo de un punto de corte
def crossover_ciclico (padre1, padre2):
    num = random.randrange(0,100)
    if num > (probabilidad_crossover*100):
        hijo1 = padre1
        hijo2 = padre2
    else:
        hijo1 = [-1] * len(padre2)
        hijo2 = [-1] * len(padre2)
        index = 0
        while padre2[index] not in hijo1: 
            hijo1.append(padre1[index])
            index = padre1.index(padre2[index])
            hijo1[index].append(padre1[index])
            index += 1

        index2 = 0
        while padre1[index2] not in hijo2:
            hijo1.append(padre1[index2])
            index2 = padre1.index(padre2[index2])
            hijo1[index2].append(padre1[index2])
            index2 += 1

    return hijo1, hijo2

#Funcion que realiza la mutacion de un cromosoma, inverte dos cromosomas random de lugar
def mutacion (hijo): 
    index = random.sample(hijo,2)
    hijo[index[0]], hijo[index[1]] = hijo[index[1]], hijo[index[0]]
    return hijo

#Funcion que calcula el fitness de cada uno de los cromosomas de la poblacion, en este caso el fitness es igual a la funcion objetivo
def fitness(poblacion):
    print("test")


#Funcion que selecciona un cromosoma de la poblacion mediante el metodo de la ruleta
def ruleta(fitness, poblacion):
    randomNum = random.random()
    acum = 0
    indiceCromosoma = 0
    for i in range(len(fitness)):
        if randomNum > acum and randomNum < (acum + fitness[i]):
            indiceCromosoma = i
            break  
        acum += fitness[i]
    return poblacion[indiceCromosoma]

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

#Funcion que selecciona los dos cromosomas/20% con mayor valor de la poblacion
def elitismo(poblacion,fitnessPoblacion):
    #Obtengo los dos cromosomas con mayor valor
    fitness_acomodado = sorted(fitnessPoblacion,reverse=True)
    maximos = fitness_acomodado[:2]
    cromosomas = []
    for i in range(2):
        indice = fitnessPoblacion.index(maximos[i])
        cromosomas.append(poblacion[indice])
    cromosoma1 = cromosomas[0]
    cromosoma2 = cromosomas[1]
    return cromosoma1, cromosoma2

#Funcion que genera una nueva poblacion en base a la poblacion anterior y sus fitness aplicando o no elitismo y ruleta o torneo
def generar_nueva_poblacion(poblacion, fitnessPoblacion, boolElitismo, boolRuleta):
    global cant_poblacion
    poblacion2= []
    recorrido = (cant_poblacion//2)
    if boolElitismo == True:
        cromosoma1, cromosoma2 = elitismo(poblacion, fitnessPoblacion)
        poblacion2.append(cromosoma1)
        poblacion2.append(cromosoma2)
        recorrido = ((cant_poblacion//2) -1)
    for i in range(recorrido): 
        if boolRuleta == True:
            padre1 = ruleta(fitnessPoblacion,poblacion)
            padre2 = ruleta(fitnessPoblacion,poblacion)
        else: 
            padre1 = torneo(fitnessPoblacion,poblacion)
            padre2 = torneo(fitnessPoblacion,poblacion)
        hijo1, hijo2 = crossover(padre1, padre2)
        hijo1 = mutacion(hijo1)
        hijo2 = mutacion(hijo2)
        poblacion2.append(hijo1)
        poblacion2.append(hijo2)
    return poblacion2


#-----------------------------------------MAIN-----------------------------------------

if len(sys.argv) != 5 or sys.argv[1] != "-s" or sys.argv[3] != "-e":
  print("Uso: python <nombre_archivo>.py -s <metodo_seleccion> -e <elitismo on/off>")
  print("metodo seleccion: 1-ruleta, 2-torneo")
  print("Elitismo: 0=off/desactivado, 1=on/activado")
  sys.exit(1)


metodo_seleccion = sys.argv[2]
opcion_elitismo = sys.argv[4]


if metodo_seleccion == '1':
    boolRuleta = True
elif metodo_seleccion == '2':
    boolRuleta = False

if opcion_elitismo == '0':
    boolElitismo = False
elif opcion_elitismo == '1':
    boolElitismo = True


#VARIABLE INICIALES
cant_poblacion = 10
cant_genes = len(bin(2**30-1))-2 #-2 para quitarle el 0b al principio
probabilidad_crossover = 0
probabilidad_mutacion = 0
maxiteraciones = 100

poblacion = []
cromosoma = []

datos_valores = []
datos_poblacionales = []
maxCromosoma = []

#Creacion de la poblacion
crear_poblacion(cant_poblacion, cant_genes)

#iteraciones
for iteraciones in range(maxiteraciones):
    fitnessPoblacion = []
    fitnessPoblacion = fitness(poblacion)
    poblacion = generar_nueva_poblacion(poblacion, fitnessPoblacion, boolElitismo, boolRuleta)


print("cromosoma con valor maximo:")
print(maxCromosoma)
print(bin_to_dec(maxCromosoma))

