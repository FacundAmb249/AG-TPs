#Falta corregir el metodo de mutacion y que se ejecute varias veces (ademas de hacer mas legible el codigo)

import random

def bin_to_dec(cromosoma):
    dec = 0
    for i in range(len(cromosoma)):
        dec += cromosoma[i]*2**(len(cromosoma)-1-i) 
    return dec

def crear_poblacion(cant_poblacion, cant_genes):
    for i in range(cant_poblacion):
      for j in range(cant_genes):
          cromosoma.append(random.randint(0,1))
      poblacion.append(cromosoma[:])
      cromosoma.clear()
    return poblacion

def crossover (padre1, padre2):
    num = random.randrange(0,100)
    if num > (probabilidad_crossover*100):
        hijo1 = padre1
        hijo2 = padre2
    else:
        punto_corte = random.randint(1,cant_genes-1)
        hijo1 = padre1[:punto_corte] + padre2[punto_corte:]
        hijo2 = padre2[:punto_corte] + padre1[punto_corte:]
        print(f"punto de corte {punto_corte}")
        # print(f"padre1 {padre1} y \npadre2 {padre2}")
        # print(f"hijo1 {hijo1} y \nhijo2 {hijo2}")
    print(f"numero aleatorio {num} y probalidad_crossover {probabilidad_crossover*100}" )
    return hijo1, hijo2

def mutacion (hijo): #esta mal la mutacion, se debia tomar un subconjunto de los genes y voltearlo
    num = random.randrange(0,100)
    print(f"numero aleatorio {num} y probabilidad_mutacion {probabilidad_mutacion*100}" )
    if num < (probabilidad_mutacion*100):
        punto_mutacion = random.randint(0,cant_genes-1)
        hijo[punto_mutacion] = 1 - hijo[punto_mutacion]
    return hijo

# prueba = bin(2**30-1)
# print(prueba)
# print(len(prueba)-2) este me da el largo del numero binario

#variable inciales
cant_poblacion = 4 #puse 4 y no 10 para que sea mas facil de ver y verificar que todo ande bien
cant_genes = len(bin(2**30-1))-2
probabilidad_crossover = 0.75
probabilidad_mutacion = 0.05
poblacion = []
cromosoma = []
valores = []
datos_poblacionales = []
datos_valores = []
valores_funcion = []
poblacion2= []

#creacion de la poblacion
crear_poblacion(cant_poblacion, cant_genes)
print("poblacion inicial:")
print(poblacion)

#pasar valores de binario a decimal, usarlo en la funcion y guardar los valores incluyendo los max, min y promedio antes y luego de la funcion
for i in range(cant_poblacion):
    valores.append(bin_to_dec(poblacion[i]))
    valores_funcion.append((bin_to_dec(poblacion[i])/(2**30-1))**2)
print("valores antes de la funcion:")
print(valores)
print("valores despues de la funcion:")
print(valores_funcion)
datos_poblacionales.append([max(valores),min(valores),sum(valores)/cant_poblacion])
datos_valores.append([max(valores_funcion),min(valores_funcion),sum(valores_funcion)/cant_poblacion])
print("datos max, min y promedio antes de la funcion:")
print(datos_poblacionales)
print("datos max, min y promedio despues de la funcion:")
print(datos_valores)

#calcular la probabilidad de seleccion de cada una de los cromosomas
probabilidad_seleccion = []
for i in range(cant_poblacion):
    probabilidad_seleccion.append(valores_funcion[i]/sum(valores_funcion))
print("probabilidad de seleccion:")
print(probabilidad_seleccion)

#ruleta
#print(random.choices(poblacion, probabilidad_seleccion, k=1))
#el primer valor son los cromosomas para elegir y el segundo para la probabilidad de eleccion correspondiente con los cromosomas
#el [0] es para que no me devuelva una lista. el k=1 es para que me devuelva un solo valor.

for i in range(cant_poblacion//2): #hay que preguntar si esta bien el //2 y que la cantidad de poblacion sea par. Pues si el numero es impar la cantidad de la poblacion disminuye en 2
    padre1 = random.choices(poblacion, probabilidad_seleccion, k=1)[0]
    padre2 = random.choices(poblacion, probabilidad_seleccion, k=1)[0]
    hijo1, hijo2 = crossover(padre1, padre2)
    hijo1 = mutacion(hijo1)
    hijo2 = mutacion(hijo2)
    poblacion2.append(hijo1)
    poblacion2.append(hijo2)
    print("padres:")
    print(padre1)
    print(padre2)
    print("hijos:")
    print(hijo1)
    print(hijo2)

poblacion = poblacion2
print("resultado final:")
print(poblacion)
