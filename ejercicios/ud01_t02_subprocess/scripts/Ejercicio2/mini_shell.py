import sys
import subprocess

nombre_fichero = "alias.txt"
alias = {}
with open(nombre_fichero, "r") as fichero:
    alias = {k:v for k,v in list(map(lambda linea: linea.strip("\n").split("="),fichero.readlines()))}


#     #meter cosas en diccionario alias
#     # for linea in fichero.readlines():
#     #     #separar la linea en dos partes y meter en el diccionario clave = valor
#     #     k,v = linea.strip("\n").split("=")
#     #     alias[k] = v

print(alias)
    