import threading
import time



class TareaContador(threading.Thread):
    def __init__(self,nombre):
        super().__init__(name=nombre)
    def run(self):
        try:
            for i in range(1,101):
                print(f"{self.args} {self.ident}: {i}")
                time.sleep(0.1)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    inicio =  time.perf_counter()
    hilo1 = TareaContador(nombre= "Mihilo-1")
    hilo2 = TareaContador(nombre= "Mihilo-2")
    hilo3 = TareaContador(nombre= "Mihilo-3")
    hilo4 = TareaContador(nombre= "Mihilo-4")
    hilo5 = TareaContador(nombre= "Mihilo-5")

    hilos = []
    hilos.append(hilo1)
    hilos.append(hilo2)
    hilos.append(hilo3)
    hilos.append(hilo4)
    hilos.append(hilo5)
    
    print("Iniciando Hilos:")
    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()
    fin = time.perf_counter()
    print(f"El programa ha tardado: {fin - inicio}")