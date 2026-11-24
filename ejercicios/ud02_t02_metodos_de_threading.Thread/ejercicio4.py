import threading
import time



class TareaContador(threading.Thread):
    def __init__(self,args):
        super().__init__()
        self.args = args
    def run(self):
        try:
            for i in range(1,101):
                print(f"{self.args}: {i}")
                time.sleep(0.1)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    inicio =  time.time()
    hilo1 = TareaContador(args= "Mihilo-1")
    hilo2 = TareaContador(args= "Mihilo-2")
    hilo3 = TareaContador(args= "Mihilo-3")
    hilo4 = TareaContador(args= "Mihilo-4")
    hilo5 = TareaContador(args= "Mihilo-5")

    hilos = []
    hilos.append(hilo1)
    hilos.append(hilo2)
    hilos.append(hilo3)
    hilos.append(hilo4)
    hilos.append(hilo5)
    
    print("Iniciando Hios:")
    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()