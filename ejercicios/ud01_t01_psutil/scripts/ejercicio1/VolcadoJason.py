#Guardar información del sistema:
import psutil

{
  "OS": "Windows",
  "CPU": {
    "Nucleos": 8,
    "Frecuencia": {
      "Freq_max": 3600.0,
      "Freq_min": 0.0,
      "Freq_current": 3600.0
    },
    "Uso_CPU": 9.3
  },
  "Memoria": {
    "Memoria_total": 17124343808,
    "memoria_disponible": 6301790208,
    "Porcentage_usada": 63.2
  },
  "Discos": {
    "Particiones": {
      "particion_0": {
        "device": "C:\\",
        "mountpoint": "C:\\",
        "fstype": "NTFS"
      },
      "particion_1": {
        "device": "G:\\",
        "mountpoint": "G:\\",
        "fstype": "FAT32"
      }
    },
    "Lecturas_disco": {
      "Disco_0": {
        "Numero_lecturas": 20423015,
        "bytes_leidos": 233889726464,
        "Numero_escrituras": 4242842,
        "bytes_escritos": 193708031488
      }
    }
  },
  "Estadisticas_Red": {
    "Gb_enviados": 11495454683,
    "Gb_recibidos": 8336004856,
    "Paquetes_enviados": 12334278,
    "Paquetes_recibidos": 13435538
  }
}
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "-system-info.json"), "w") as fichero:
     json.dump(data, fichero, indent=2)


