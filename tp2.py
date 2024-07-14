import sys

# Funcion que transforma binario a decimal
def bin_to_dec(cromosoma):
    dec = 0
    for i in range(len(cromosoma)):
        dec += cromosoma[i]*2**(len(cromosoma)-1-i)
    return dec

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

busqueda = int(sys.argv[2])
lista = int(sys.argv[4])

lista_1a = [150, 325, 600, 805, 430, 1200, 770, 60, 930, 353] # cm³
lista_1b = [20, 40, 50, 36, 25, 64, 54, 18, 46, 28] # $
max_1 = 4200 # cm³
lista_2a = [1800, 600, 1200] # grs.
lista_2b = [72, 36, 60] # $
max_2 = 3600 # grs.
