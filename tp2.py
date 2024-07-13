import sys

# Funcion que transforma binario a decimal
def bin_to_dec(cromosoma):
    dec = 0
    for i in range(len(cromosoma)):
        dec += cromosoma[i]*2**(len(cromosoma)-1-i)
    return dec

# Main
if len(sys.argv) != 5 or sys.argv[1] != "-b" or sys.argv[3] != "-o":
  print("python tp2.py -b <tipo_busqueda> -o <tipo_val>")
  print("")
  print("-b 0 : busqueda exhaustiva")
  print("-b 1 : busqueda golosa")
  print("-o 0 : evaluar usando volumen (cm³)")
  print("-o 1 : evaluar usando peso (grs.)")
  sys.exit(1)

tipo_busqueda = sys.argv[2]
tipo_val = sys.argv[4]

lista_a1 = [150, 325, 600, 805, 430, 1200, 770, 60, 930, 353] # cm³
lista_a2 = [20, 40, 50, 36, 25, 64, 54, 18, 46, 28] # $
max_a = 4200 # cm³
lista_b1 = [1800, 600, 1200] # grs.
lista_b2 = [72, 36, 60] # $
max_b = 3600 # grs.
