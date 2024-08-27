import pandas #para armar la tabla de datos del final
import sys

#matrizObjetos[0] -> Numero objeto
#matrizObjetos[1] -> Volumen o Peso objeto
#matrizObjetos[2] -> Valor monetario objeto

#Ordena de mayor a menor
def ordenaDesc(matrizObjetos, cantObjetos):
  for i in range(cantObjetos):
    for j in range(i+1, cantObjetos):
      if (matrizObjetos[2][i] / matrizObjetos[1][i]) < (matrizObjetos[2][j] / matrizObjetos[1][j]):
        #invierte la posición de ambos valores
        matrizObjetos[0][i], matrizObjetos[0][j] = matrizObjetos[0][j], matrizObjetos[0][i]
        matrizObjetos[1][i], matrizObjetos[1][j] = matrizObjetos[1][j], matrizObjetos[1][i]
        matrizObjetos[2][i], matrizObjetos[2][j] = matrizObjetos[2][j], matrizObjetos[2][i]

def greedyBusqueda(matrizObjetos, maxVolumenPeso, cantObjetos):
  mayorValor = 0 
  mayorPesoVolumen = 0
  objetosEnMochila = [] 
  ordenaDesc(matrizObjetos, cantObjetos)
  for i in range(cantObjetos):
    if mayorPesoVolumen + matrizObjetos[1][i] <= maxVolumenPeso:
      mayorPesoVolumen  += matrizObjetos[1][i]
      mayorValor += matrizObjetos[2][i]
      objetosEnMochila.append([matrizObjetos[0][i], matrizObjetos[1][i], matrizObjetos[2][i]])
  return objetosEnMochila, mayorPesoVolumen, mayorValor

def exhaustivaBusqueda(matrizObjetos,maxVolumenPeso, cantObjetos): 
    combinacionObjetos = [-1] * cantObjetos
    algoritmo_backtracking(combinacionObjetos,maxVolumenPeso, 0, cantObjetos)
    return valorCombinacion(matrizObjetos,maxVolumenPeso, cantObjetos)

#Genera todas las combinaciones posibles de elementos, mediante recursividad, las guarda en un lista 'subConjunto'
def algoritmo_backtracking(combinacionObjetos, maxVolumenPeso, i, cantObjetos):
    if i == cantObjetos:
        subConjunto.append(combinacionObjetos[:])
        return

    combinacionObjetos[i] = 0
    algoritmo_backtracking(combinacionObjetos,maxVolumenPeso, i + 1, cantObjetos)

    combinacionObjetos[i] = 1
    algoritmo_backtracking(combinacionObjetos,maxVolumenPeso, i + 1, cantObjetos)

#Recorre el subConjunto de combinaciones, encuentra el que tiene mayor valor y cumple con la restriccion propuesta
def valorCombinacion(matrizObjetos, maxVolumenPeso, cantObjetos):
  mayorPesoVolumen = 0
  mayorValor = 0
  objetosEnMochila = []

  for i in range (0, len(subConjunto)):
    locValorMochila = 0 
    locVolumenPesoMochila = 0
    locObjetosMochila = []
    for j in range (0, cantObjetos):
      if subConjunto[i][j] == 1:
        locVolumenPesoMochila += matrizObjetos[1][j]
        locValorMochila += matrizObjetos[2][j]
        locObjetosMochila.append([matrizObjetos[0][j], matrizObjetos[1][j], matrizObjetos[2][j]])

    if (locVolumenPesoMochila <= maxVolumenPeso):
      if (locValorMochila > mayorValor):
        mayorValor = locValorMochila
        mayorPesoVolumen = locVolumenPesoMochila
        objetosEnMochila = locObjetosMochila[:]
  return objetosEnMochila, mayorPesoVolumen, mayorValor


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
  sys.exit(1)


#Inicialización de variables
lista_1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [150, 325, 600, 805, 430, 1200, 770, 60, 930, 353], [20, 40, 50, 36, 25, 64, 54, 18, 46, 28]] #pos, cm³, $
maxVolumenPeso_1 = 4200 #cm³
lista_2 = [[1, 2, 3], [1800, 600, 1200], [72, 36, 60]] #pos, grs., $
maxVolumenPeso_2 = 3000 #grs.
subConjunto = []

if sys.argv[4] == '1':
  matrizObjetos = lista_1
  maxVolumenPeso= maxVolumenPeso_1
  cantObjetos = len(lista_1[0])
  columnas = ["N. objeto", "Volúmen (cm³)", "Valor ($)"]
  unidad = "cm³"
elif sys.argv[4] == '2':
  matrizObjetos = lista_2
  maxVolumenPeso= maxVolumenPeso_2
  cantObjetos = len(lista_2[0])
  columnas = ["N. objeto", "Peso (grs.)", "Valor ($)"]
  unidad = "grs."


if sys.argv[2] == '1': #Búsqueda exhaustiva
  objetosEnMochila, mayorPesoVolumen, mayorValor = exhaustivaBusqueda(matrizObjetos, maxVolumenPeso, cantObjetos)
elif sys.argv[2] == '2': #Búsqueda greedy (golosa)
  objetosEnMochila, mayorPesoVolumen, mayorValor = greedyBusqueda(matrizObjetos, maxVolumenPeso, cantObjetos)

datos = pandas.DataFrame(objetosEnMochila, columns=columnas)
print(datos)
print("Capacidad total =", maxVolumenPeso, unidad)
print("Peso total =", mayorPesoVolumen , unidad)
print("Precio final = $", mayorValor)
