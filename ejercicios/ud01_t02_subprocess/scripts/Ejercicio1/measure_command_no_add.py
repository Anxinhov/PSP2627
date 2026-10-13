# ejemplo de uso: python mesure command.py ping as.com

import sys
import subprocess
import time
argumentos = sys.argv[1:]
print(f"""Ejecutando: {"".join(argumentos)}
Salida del proceso:""")
inicio = time.perf_counter()
resultado = subprocess.run(argumentos, shell=True)
fin = time.perf_counter()
print(f"""
{resultado.stdout}
{resultado.stderr}

Tiempo de ejecución: {(fin-inicio):2.2f} segundos
Código de salida: {resultado.returncode}
""")