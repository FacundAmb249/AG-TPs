# Importar clases aquí

# Funcion que transforma binario a decimal
def bin_to_dec(cromosoma):
    dec = 0
    for i in range(len(cromosoma)):
        dec += cromosoma[i]*2**(len(cromosoma)-1-i)
    return dec

# Main
if len(sys.argv) != 5 or sys.argv[1] != "-b" or sys.argv[3] != "-o":
  print("python tp2.py -b <tipo_busqueda> -o <elitismo on/off>")
  print("")
  print("-b 0 : busqueda exhaustiva")
  print("-b 1 : busqueda golosa")
  print("-o 0 : evaluar usando volumen (cm³)")
  print("-o 1 : evaluar usando peso (grs.)")
  sys.exit(1)
