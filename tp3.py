import sys
import csv
from distancias import cargar_distancias
from metodo_heuristico import metodo_heuristico_con_origen

#python3 tp3.py -h -o/so
#python3 tp3.py -g  

#Validacion de menu 
if (sys.argv[1] != "-h" and sys.argv[1] != "-g") :
    print("Opciones invalidas, ingrese alguna de las siguientes opciones")
    print("python main.py -h -o : metodo heuristico con origen")
    print("python main.py -h -so : metodo heuristico sin origen")
    print("python main.py -g : metodo genetico")
    sys.exit(1)

ciudades, distancias = cargar_distancias()

#Agregar menu para elegir la ciudad de partida. indice_ciudad de la ciudad de partida

if sys.argv[1] == "-h":
    if sys.argv[2] == "-o":
        z = metodo_heuristico_con_origen(distancias,ciudades,0) 

    elif sys.argv[2] == "so":
        z = metodo_heuristico_sin_origen 

elif sys.argv[1] == "g":
    x = metodo_genetico(distancias, ciudades, indice_ciudad)
