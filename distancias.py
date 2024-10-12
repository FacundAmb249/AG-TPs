import csv


def cargar_distancias():
    ciudades = [] 
    distancias = []
    with open('tabla_distancias.csv', newline='') as f: 
        reader = csv.reader(f)
        data = list(reader)
        for line in data:
            ciudades.append(line[0])
            distancias.append([0 if cell == '' else int(cell) for cell in line[1:]])

    return ciudades, distancias



