import folium
# Coordenadas (latitud, longitud) de las capitales de provincias argentinas

ciudades = {
    0:[-34.6118, -58.4173],
    1:[-31.4201, -64.1888],
    2:[-27.4800, -58.8340],
    3:[-26.1865, -58.1745],
    4:[-34.9207, -57.9538],
    5:[-29.4135, -66.8562],
    6:[-32.8902, -68.8440],
    7:[-38.9516, -68.0591],
    8:[-31.7446, -60.5118],
    9:[-27.3621, -55.9007],
    10:[-43.3000, -65.1023],
    11:[-27.4510, -58.9867],
    12:[-51.6230, -69.2168],
    13:[-28.4696, -65.7852],
    14:[-26.8083, -65.2176],
    15:[-24.1858, -65.2995],
    16:[-24.7828, -65.4128],
    17:[-31.5375, -68.5364],
    18:[-33.2772, -66.3200],
    19:[-31.6333, -60.7000],
    20:[-36.6229, -64.2953],
    21:[-27.7951, -64.2615],
    22:[-54.8019, -68.3029],
    23:[-40.8135, -63.0000],
}

def ruta_mapa(recorrido):
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
