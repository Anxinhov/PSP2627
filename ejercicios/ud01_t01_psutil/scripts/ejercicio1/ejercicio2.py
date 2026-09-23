#Información de CPUs
import psutil
#Número de CPUs
print(psutil.cpu_count())
#Frecuencia de cada CPU
print(psutil.cpu_percent(interval=1))
#Uso de CPU por CPUs
print (psutil.cpu_freq())