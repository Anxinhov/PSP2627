#Información de discos
import psutil
#Listado de particiones
print(psutil.disk_partitions(all=False))
#Uso de disco para cada unidad o partición
print(psutil.disk_usage('/'))
#Número de operaciones de lectura
print(psutil. disk_io_counters().read_count)
#Número de operaciones de escritura
print(psutil. disk_io_counters().write_count)
#Número de bytes leídos
print(psutil. disk_io_counters().read_bytes)
#Número de bytes escritos
print(psutil. disk_io_counters().write_bytes)