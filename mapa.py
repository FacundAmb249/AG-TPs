import folium
# Coordenadas (latitud, longitud) de las capitales de provincias argentinas
ciudades = {
    0: [-34.603722, -58.381592],  
    1: [-28.469581, -65.779545],
    2: [-31.416668, -64.183334],
    3: [-27.471221, -58.839584],
    4: [-26.18489, -58.17313],
    5: [-34.9204948, -57.9535657],  
    6: [-29.41105, -66.85067],
    7: [-32.89084, -68.82717],
    8: [-38.95161, -68.0591],
    9: [-31.73197, -60.5238], 
    10: [-27.36244, -55.90084],
    11: [-43.30016, -65.10228],  
    12: [-27.45157, -58.98656],  
    13: [-51.62261, -69.21813],  
    14: [-24.782932, -65.423851],
    15: [-28.469581, -65.779545],
    16: [-31.5375, -68.53639],
    17: [-33.29501, -66.33563],
    18: [-26.80828, -65.21759],
    19: [-24.18579, -65.29952],
    20: [-31.63333, -60.7],
    21: [-36.61667, -64.28333],  
    22: [-27.79511, -64.26149],
    23: [-54.80191, -68.30295],  
    24: [-40.81345, -62.99668]  
}

# Ejemplo de recorrido: supongamos que este es el orden del recorrido
recorrido = [0,1,2,3,4]

# Crear un mapa centrado en la primera ciudad del recorrido
mapa = folium.Map(location=ciudades[recorrido[0]], zoom_start=6)

# Añadir marcadores para cada ciudad en el recorrido
for ciudad in recorrido:
    folium.Marker(ciudades[ciudad]).add_to(mapa)

coordenadas_recorrido = [ciudades[ciudad] for ciudad in recorrido]

#Linea del mapa 
folium.PolyLine(coordenadas_recorrido, color='blue', weight=2.5, opacity=1).add_to(mapa)

mapa.save('recorrido_argentina.html')

print("Mapa creado y guardado como 'recorrido_argentina.html'")
