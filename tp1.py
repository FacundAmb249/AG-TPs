#Falta corregir el metodo de mutacion y que se ejecute varias veces (ademas de hacer mas legible el codigo)

import random
import matplotlib.pyplot as plt
import pandas as pd
import sys
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)


#Funcion que transforma binario a decimal
def bin_to_dec(cromosoma):
    dec = 0
    for i in range(len(cromosoma)):
        dec += cromosoma[i]*2**(len(cromosoma)-1-i) 
    return dec

#Funcion que crea la poblacion inicial en base a la cantidad de poblacion inicial y cant_genes
def crear_poblacion(cant_poblacion, cant_genes):
    for _ in range(cant_poblacion):
        cromosoma = [random.randint(0, 1) for i in range(cant_genes)]
        poblacion.append(cromosoma)
    return poblacion

#Funcion que elige un cromosoma en base a su probabilidad (fitness)
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

def crossover (padre1, padre2):
    num = random.randrange(0,100)
    if num > (probabilidad_crossover*100):
        hijo1 = padre1
        hijo2 = padre2
    else:
        punto_corte = random.randint(1,cant_genes-1)
        hijo1 = padre1[:punto_corte] + padre2[punto_corte:]
        hijo2 = padre2[:punto_corte] + padre1[punto_corte:]
    return hijo1, hijo2

def mutacion (hijo): #No se si los punto donde se hace la mutacion son correctos para el caso que el punto1 sea igual al comienzo (posicion 0) y punto2 sea igual al final (posicion 5)
    num = random.randrange(0,100)
    if num < (probabilidad_mutacion*100):
        punto1 = random.randint(0,cant_genes-1)
        punto2 = random.randint(0,cant_genes-1)
        #si los puntos son iguales o consecutivos se vuelve a buscar, ya que sino el cromosoma queda igual
        while punto1 == punto2 or abs(punto1 - punto2) == 1:
            punto1 = random.randint(0, len(hijo) - 1)
            punto2 = random.randint(0, len(hijo) - 1)
        print(f"punto1 {punto1} y punto2 {punto2}")
        if punto1 > punto2:
            punto1, punto2 = punto2, punto1
        hijo = hijo[:punto1] + hijo[punto1:punto2][::-1] + hijo[punto2:]
    return hijo

def fitness(poblacion):
    global maxCromosoma
    global datos_poblacionales
    global datos_valores
    valores_funcion = []
    valores = []
    #Obtengo el cromosoma con mayor valor de la poblacion
    if maxCromosoma < max(poblacion):
        maxCromosoma = max(poblacion)
    #Guardo los valores de los cromosomas en decimal y en funcion de la poblacion
    for cromosoma in poblacion:
        valores.append(bin_to_dec(cromosoma))
        valores_funcion.append((bin_to_dec(cromosoma)/(2**30-1))**2)
    print("valores decimales antes de aplicar la funcion:")
    print(valores)
    print("valores despues de aplicar la funcion:")
    print(valores_funcion)
    
    #Guardo los valores maximos, minimos y promedios de la poblacion
    datos_poblacionales.append([max(valores),min(valores),int(sum(valores)/len(valores)),max(poblacion)])
    datos_valores.append([max(valores_funcion),min(valores_funcion),sum(valores_funcion)/len(valores_funcion)])
    print(f"la cantidad de poblacion es: {cant_poblacion}")

    #Calcula el fitness de cada una de los cromosomas
    for i in range(cant_poblacion):
        fitnessPoblacion.append(valores_funcion[i]/sum(valores_funcion))
    return fitnessPoblacion



#Funcion que genera una nueva poblacion en base a la ruleta y sin elitismo
def generar_nueva_poblacion_ruleta_sin_elitismo(poblacion, fitnessPoblacion):
    global cant_poblacion
    poblacion2= []
    for i in range((cant_poblacion//2) ): 
        padre1 = ruleta(fitnessPoblacion,poblacion)
        padre2 = ruleta(fitnessPoblacion,poblacion)
        hijo1, hijo2 = crossover(padre1, padre2)
        hijo1 = mutacion(hijo1)
        hijo2 = mutacion(hijo2)
        poblacion2.append(hijo1)
        poblacion2.append(hijo2)
    return poblacion2

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

def generar_nueva_poblacion_ruleta_con_elitismo(poblacion,fitnessPoblacion):
    global cant_poblacion
    poblacion2= []
    cromosoma1, cromosoma2 = elitismo(poblacion, fitnessPoblacion)
    poblacion2.append(cromosoma1)
    poblacion2.append(cromosoma2)
    for i in range((cant_poblacion//2)-1): 
        padre1 = ruleta(fitnessPoblacion,poblacion)
        padre2 = ruleta(fitnessPoblacion,poblacion)
        hijo1, hijo2 = crossover(padre1, padre2)
        hijo1 = mutacion(hijo1)
        hijo2 = mutacion(hijo2)
        poblacion2.append(hijo1)
        poblacion2.append(hijo2)
    return poblacion2

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

def generar_nueva_poblacion_torneo_sin_elitismo(poblacion,fitnessPoblacion):
    global cant_poblacion
    poblacion2= []
    for i in range((cant_poblacion//2) ): 
        padre1 = torneo(fitnessPoblacion,poblacion)
        padre2 = torneo(fitnessPoblacion,poblacion)
        hijo1, hijo2 = crossover(padre1, padre2)
        hijo1 = mutacion(hijo1)
        hijo2 = mutacion(hijo2)
        poblacion2.append(hijo1)
        poblacion2.append(hijo2)
    return poblacion2

def generar_nueva_poblacion_torneo_con_elitismo(poblacion,fitnessPoblacion):
    global cant_poblacion
    poblacion2= []
    cromosoma1, cromosoma2 = elitismo(poblacion, fitnessPoblacion)
    poblacion2.append(cromosoma1)
    poblacion2.append(cromosoma2)
    for i in range((cant_poblacion//2)-1): 
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

#VARIABLE INICIALES
cant_poblacion = 10 
cant_genes = len(bin(2**30-1))-2 #-2 para quitarle el 0b al principio
probabilidad_crossover = 0.75
probabilidad_mutacion = 0.05
maxiteraciones = 1

poblacion = []
cromosoma = []

datos_valores = []
datos_poblacionales = []
maxCromosoma = []

if metodo_seleccion == "1":
    #Creacion de la poblacion
    poblacion = crear_poblacion(cant_poblacion, cant_genes)
    print("poblacion inicial:")
    print(poblacion)
    if opcion_elitismo == "0":
        print("Se selecciono ruleta sin elitismo")
        #iteraciones
        for iteraciones in range(maxiteraciones):
            print("-------------------------------------------------------------------------------------------------")
            fitnessPoblacion = []
            fitnessPoblacion = fitness(poblacion)
            poblacion = generar_nueva_poblacion_ruleta_sin_elitismo(poblacion, fitnessPoblacion)
            print(f"poblacion en la iteracion {iteraciones+1}: {poblacion}")
    else:
        print("Se selecciono ruleta con elitismo")
        #iteraciones
        for iteraciones in range(maxiteraciones):
            print("-------------------------------------------------------------------------------------------------")
            fitnessPoblacion = []
            fitnessPoblacion = fitness(poblacion)
            poblacion = generar_nueva_poblacion_ruleta_con_elitismo(poblacion, fitnessPoblacion)
            print(f"poblacion en la iteracion {iteraciones+1}: {poblacion}")
elif metodo_seleccion == "2":
    #Creacion de la poblacion
    poblacion = crear_poblacion(cant_poblacion, cant_genes)
    print("poblacion inicial:")
    print(poblacion)

    if opcion_elitismo == "0":
        print("Se selecciono torneo sin elitismo")
        #iteraciones
        for iteraciones in range(maxiteraciones):
            print("-------------------------------------------------------------------------------------------------")
            fitnessPoblacion = []
            fitnessPoblacion = fitness(poblacion)
            poblacion = generar_nueva_poblacion_torneo_sin_elitismo(poblacion, fitnessPoblacion)
            print(f"poblacion en la iteracion {iteraciones+1}: {poblacion}")
    else:
        print("Se selecciono torneo con elitismo")
        #iteraciones
        for iteraciones in range(maxiteraciones):
            print("-------------------------------------------------------------------------------------------------")
            fitnessPoblacion = []
            fitnessPoblacion = fitness(poblacion)
            poblacion = generar_nueva_poblacion_torneo_con_elitismo(poblacion, fitnessPoblacion)
            print(f"poblacion en la iteracion {iteraciones+1}: {poblacion}")
else:
    print("Estrategia de seleccion invalida o elitismo invalido")
    sys.exit(1)

print("cromosoma con valor maximo:")
print(maxCromosoma)
print(bin_to_dec(maxCromosoma))

# Crear un DataFrame(tabla) con los datos de la población
Columnas = ['Maximos', 'Minimos', 'Promedios','cromosoma del maximo']
df = pd.DataFrame(datos_poblacionales, columns=Columnas,index=list(range(1,maxiteraciones+1)))
print(df)

# Crear los graficos de los datos
ejex= list(range(maxiteraciones))
valores_maximos = [val[0] for val in datos_valores]
valores_minimos = [val[1] for val in datos_valores]
valores_promedios = [val[2] for val in datos_valores]
# Grafica de la funcion objetivo para n interaciones
plt.figure(1)
plt.plot(ejex, valores_maximos,label='valores maximos')
plt.plot(ejex, valores_minimos,label='valores minimos')
plt.plot(ejex, valores_promedios,label='valores promedios')
plt.title('Valores maximo, minimo y prom de la funcion en cada iteracion')
plt.legend()
plt.show()

