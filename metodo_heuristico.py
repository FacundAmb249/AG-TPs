




num_ciudades = 24


def metodo_heuristico_con_origen(distancias, ciudades, origen):
    ocupados = [0] * len(ciudades)  
    recorrido = []
    count = 0
    ciudad = origen
    num_ciudades = len(ciudades)  

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
            ciudad = ciudadCercana  
            ocupados[ciudadCercana] = 1  
            count += 1  
        else:
            break  

    # Vuelve al origen
    recorrido.append(origen)

    print("Recorrido completo:", recorrido)

    return recorrido
    
