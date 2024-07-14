import sys

#Cantidad de elementos para $ máximo para un volumen maxLista
#Se podría pasar a una colección de datos para tener una sola variable de lista.

#Ordena de mayor a menor
def ordenaDesc(lista_a, lista_b, lista_c):
  for i in range(len(lista_a)):
    for j in range(i+1, len(lista_a)):
      if lista_c[i] < lista_c[j]:
        lista_a[i], lista_a[j] = lista_a[j], lista_a[i]
        lista_b[i], lista_b[j] = lista_b[j], lista_b[i]
        lista_c[i], lista_c[j] = lista_c[j], lista_c[i]

def greedyBusqueda(lista_a, lista_b, lista_c, maxLista):
  ordenaDesc(lista_a, lista_b, lista_c)
  for i in range(len(lista_a)):
    if vpMochila + lista_b[i] <= maxLista:
      vpMochila += lista_b[i]
      valorMochila += lista_c[i]
      elementosEnMochila_a.append(lista_a[i])
      elementosEnMochila_b.append(lista_b[i])
      elementosEnMochila_c.append(lista_c[i])

# Main
if len(sys.argv) != 5 or sys.argv[1] != "-b" or sys.argv[3] != "-l":
  print("python tp2.py -b <tipo_busqueda> -l <lista_actual>")
  print("")
  print("-b 1 : busqueda exhaustiva")
  print("-b 2 : busqueda golosa")
  print("-l 1 : lista de elementos 1 (cm³)")
  print("-l 2 : lista de elementos usando peso (grs.)")
  sys.exit(1)
elif sys.argv[2] != '1' and sys.argv[2] != '2':
  print("Opción de búsqueda inválida")
  sys.exit(1)
elif sys.argv[4] != '1' and sys.argv[4] != '2':
  print("Lista inexistente")

#Se podría pasar a una colección de datos para tener una sola variable de lista.
lista_1a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # pos
lista_1b = [150, 325, 600, 805, 430, 1200, 770, 60, 930, 353] # cm³
lista_1c = [20, 40, 50, 36, 25, 64, 54, 18, 46, 28] # $
maxLista_1 = 4200 # cm³
lista_2a = [1, 2, 3] # pos
lista_2b = [1800, 600, 1200] # grs.
lista_2c = [72, 36, 60] # $
maxLista_2 = 3600 # grs.

if sys.argv[4] = '1':
  lista_a = lista_1a
  lista_b = lista_1b
  lista_c = lista_1c
  maxLista = maxLista_1
elif sys.argv[4] = '2':
  lista_a = lista_2a
  lista_b = lista_2b
  lista_c = lista_2c
  maxLista = maxLista_2

elementosEnMochila_a = []
elementosEnMochila_b = []
elementosEnMochila_c = []
vpMochila = 0     #cm³ or grs.
valorMochila = 0  # $

if sys.argv[2] = '1': #Búsqueda exhaustiva
  #Sacar el exit cuando se complete esta sección
  print("Completar esta sección")
  sys.exit(1)
if sys.argv[2] = '2': #Búsqueda greedy (golosa)
  greedyBusqueda(lista_a, lista_b, lista_c, maxLista)
