import threading
import time
import random


class TareaContador(threading.Thread):
    def __init__(self,args):
        super().__init__()
        self.args = args
        self.tiempo = random.randint(0,10)
    def run(self):
        try:
            
            print (f"{self.args} va a estar  dormido: {self.tiempo*1000} milisegundos")
            time.sleep(self.tiempo)
            print(f"{self.args} ha despertado")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    hilo1 = TareaContador(args= "Hilo A")
    hilo2 = TareaContador(args= "Hilo B")
    hilo3 = TareaContador(args= "Hilo C")
    print("Iniciando subprocesos:")
    hilo1.start()
    hilo2.start()
    hilo3.start()
    print("Subprocesos iniciados, termina main")
    hilo1.join()
    hilo2.join()
    hilo3.join()
    