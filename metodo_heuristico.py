

num_ciudades = 24

def metodo_heuristico_sin_origen(distancias,ciudades):
    menorDistTotal = 1000000 
    menorRecorrido = []

    for ciudad in range (len(ciudades)):
        rec, distTotal = metodo_heuristico_con_origen(distancias,ciudades, ciudad)
        if distTotal < menorDistTotal:
            menorDistTotal = distTotal
            menorRecorrido = rec

    return menorRecorrido, menorDistTotal


def metodo_heuristico_con_origen(distancias, ciudades, origen):
    ocupados = [0] * len(ciudades)  
    recorrido = []
    count = 0
    ciudad = origen
    num_ciudades = len(ciudades)  
    distTotal = 0

    # Marcamos la ciudad de origen como visitada
    ocupados[ciudad] = 1
    recorrido.append(ciudad)

    while count < num_ciudades - 1:  
        minDist = 10000000  
        ciudadCercana = -1
        index = 0

        # Recorrer las distancias desde la ciudad actual
        for dist in distancias[ciudad]:
            if dist < minDist and ocupados[index] == 0 and dist != 0:
                minDist = dist
                ciudadCercana = index  
            index += 1

        if ciudadCercana != -1:
            recorrido.append(ciudadCercana)  
            distTotal += minDist
            ciudad = ciudadCercana  
            ocupados[ciudadCercana] = 1  
            count += 1  
        else:
            break  

    # Vuelve al origen
    recorrido.append(origen)

    return recorrido, distTotal
    
