import pandas #para armar la tabla de datos del final
import sys

#Cantidad de elementos para $ máximo para un volumen maxLista

#Ordena de mayor a menor
def ordenaDesc(lista):
  for i in range(len(lista[0])):
    for j in range(i+1, len(lista[0])):
      if (lista[2][i] / lista[1][i]) < (lista[2][j] / lista[1][j]):
        #invierte la posición de ambos valores
        lista[0][i], lista[0][j] = lista[0][j], lista[0][i]
        lista[1][i], lista[1][j] = lista[1][j], lista[1][i]
        lista[2][i], lista[2][j] = lista[2][j], lista[2][i]

def greedyBusqueda(lista, maxLista):
  vpMochila = 0     #cm³ or grs.
  valorMochila = 0  # $
  ordenaDesc(lista)
  for i in range(len(lista[0])):
    if vpMochila + lista[1][i] <= maxLista:
      vpMochila += lista[1][i]
      valorMochila += lista[2][i]
      elementosEnMochila.append([lista[0][i], lista[1][i], lista[2][i]])
  return elementosEnMochila, vpMochila, valorMochila

def exhaustivaBusqueda(lista,maxLista): 
    lista_inicial = [-1] * len(lista[0])
    algoritmo_backtracking(lista_inicial,maxLista, 0)
    return valorCombinacion(lista,maxLista)

#Recorre el subConjunto de combinaciones, encuentra el que tiene mayor valor y cumple con la restriccion propuesta
def valorCombinacion(lista, maxLista):
  mayValor = 0 
  totPesoVol = 0
  for i in range (0, len(subConjunto)):
    valorMochila = 0 
    vpMochila = 0
    LocElemMochila = []
    for j in range (0, len(lista[0])):
      if subConjunto[i][j] == 1:
        vpMochila += lista[1][j]
        valorMochila += lista[2][j]
        LocElemMochila.append([lista[0][j], lista[1][j], lista[2][j]])
    if (vpMochila <= maxLista):
      if (valorMochila > mayValor):
        mayValor = valorMochila
        totPesoVol = vpMochila
        elementosEnMochila = LocElemMochila[:]
  return elementosEnMochila, totPesoVol, mayValor

#Genera todas las combinaciones posibles de elementos, mediante recursividad, las guarda en un lista 'subConjunto'
def algoritmo_backtracking(lista_inicial, maxLista, i):
    if i == len(lista_inicial):
        subConjunto.append(lista_inicial[:])
        return

    lista_inicial[i] = 0
    algoritmo_backtracking(lista_inicial,maxLista, i + 1)

    lista_inicial[i] = 1
    algoritmo_backtracking(lista_inicial,maxLista, i + 1)

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
lista_1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [150, 325, 600, 805, 430, 1200, 770, 60, 930, 353], [20, 40, 50, 36, 25, 64, 54, 18, 46, 28]] #pos, cm³, $
maxLista_1 = 4200 #cm³
lista_2 = [[1, 2, 3], [1800, 600, 1200], [72, 36, 60]] #pos, grs., $
maxLista_2 = 3000 #grs.
subConjunto = []

if sys.argv[4] == '1':
  lista = lista_1
  maxLista= maxLista_1
  columnas = ["N. objeto", "Volúmen (cm³)", "Valor ($)"]
  unidad = "cm³"
elif sys.argv[4] == '2':
  lista = lista_2
  maxLista= maxLista_2
  columnas = ["N. objeto", "Peso (grs.)", "Valor ($)"]
  unidad = "grs."

elementosEnMochila = []

if sys.argv[2] == '1': #Búsqueda exhaustiva
  elementosEnMochila, vpMochila, valorMochila = exhaustivaBusqueda(lista, maxLista)
elif sys.argv[2] == '2': #Búsqueda greedy (golosa)
  elementosEnMochila, vpMochila, valorMochila = greedyBusqueda(lista, maxLista)

datos = pandas.DataFrame(elementosEnMochila, columns=columnas)
print(datos)
print("Capacidad total =", maxLista, unidad)
print("Peso total =", vpMochila, unidad)
print("Precio final = $", valorMochila)
