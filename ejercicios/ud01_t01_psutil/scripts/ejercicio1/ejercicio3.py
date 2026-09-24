#Información de memoria
import psutil
#Memoria total
print(psutil.virtual_memory().total)
#Memoria disponible
print(psutil.virtual_memory().available)
#Porcentaje de memoria usada
print(psutil.virtual_memory().percent)