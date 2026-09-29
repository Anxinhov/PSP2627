#Estadísticas de red
import psutil
#Bytes enviados
print(psutil.net_io_counters().bytes_sent)
#Bytes recibidos
print(psutil.net_io_counters().bytes_recv)
#Paquetes enviados
print(psutil.net_io_counters().packets_sent)
#Paquetes recibidos
print(psutil.net_io_counters().packets_recv)
