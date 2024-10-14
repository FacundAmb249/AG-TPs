import sys
import csv
from distancias import cargar_distancias
from metodo_heuristico import metodo_heuristico_con_origen, metodo_heuristico_sin_origen
from metodo_genetico import metodo_genetico
from mapa import ruta_mapa

#python3 tp3.py -h -o/so
#python3 tp3.py -g  

#Validacion de menu 
def info():
    print("Opciones invalidas, ingrese alguna de las siguientes opciones")
    print("python main.py -h -co : metodo heuristico con origen")
    print("python main.py -h -so : metodo heuristico sin origen")
    print("python main.py -g -ce : metodo genetico con elitismo")
    print("python main.py -g -se : metodo genetico sin elitismo")
    sys.exit(1)

if (sys.argv[1] != "-h" and sys.argv[1] != "-g") :
    info()

ciudades, distancias = cargar_distancias()

if sys.argv[1] == "-h":
    if sys.argv[2] == "-co":
        print("Ingrese el origen del recorrido, 0-23") 
        origen = int(input())

        recorrido, distancia = metodo_heuristico_con_origen(distancias,ciudades,origen)

    elif sys.argv[2] == "-so":
        recorrido, distancia = metodo_heuristico_sin_origen(distancias,ciudades)

    else:
        info()

elif sys.argv[1] == "-g":
    if sys.argv[2] == "-ce":
        recorrido, distancia = metodo_genetico(distancias, ciudades, True)
    elif sys.argv[2] == "-se":
        recorrido, distancia = metodo_genetico(distancias, ciudades, False)
    else:
        info()

else:
    info()

ruta_mapa(recorrido)
print(distancia)
print(recorrido)
ciudadTestrecorrido = []
for i in range(0,24):
    ciudadindex = recorrido[i]
    c = ciudades[ciudadindex]
    ciudadTestrecorrido.append(c)
print(ciudadTestrecorrido)
