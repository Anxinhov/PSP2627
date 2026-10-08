#Información de CPUs
import psutil
#Número de CPUs
print(psutil.cpu_count())
#Frecuencia de cada CPU
print([f.max for f in psutil.cpu_freq(percpu=True)])
#Uso de CPU por CPUs
print(psutil.cpu_times_percent(interval=1, percpu=True))