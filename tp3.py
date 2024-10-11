import sys
import csv
from distancias import cargar_distancias
from metodo_heuristico import metodo_heuristico_con_origen, metodo_heuristico_sin_origen
from metodo_genetico import metodo_genetico
from mapa import ruta_mapa

#python3 tp3.py -h -o/so
#python3 tp3.py -g  

#Validacion de menu 
if (sys.argv[1] != "-h" and sys.argv[1] != "-g") :
    print("Opciones invalidas, ingrese alguna de las siguientes opciones")
    print("python main.py -h -o : metodo heuristico con origen")
    print("python main.py -h -so : metodo heuristico sin origen")
    print("python main.py -g -o : metodo genetico")
    sys.exit(1)

ciudades, distancias = cargar_distancias()
if sys.argv[2] == "-o":
    print("Ingrese el origen del recorrido, 1-24") 
    origen = int(input())
    origen = origen - 1

if sys.argv[1] == "-h":
    if sys.argv[2] == "-o":
        recorrido, distancia = metodo_heuristico_con_origen(distancias,ciudades,origen) 
        ruta_mapa(recorrido)
        print(distancia)

    elif sys.argv[2] == "-so":
        recorrido, distancia = metodo_heuristico_sin_origen(distancias,ciudades)
        ruta_mapa(recorrido)
        print(distancia)
        print(recorrido)

elif (sys.argv[1] == "-g") and (sys.argv[2] == "-o"):
    recorrido, distancia = metodo_genetico(distancias, ciudades, origen)
