import threading
import time



class Factorial(threading.Thread):
    def __init__(self,nombre,numero):
        super().__init__(name=nombre)
        self.numero = numero
    def run(self):
        try:
            for i in range(1,101):
                print(f"{self.args} {self.ident}: {i}")
                time.sleep(0.1)
        except Exception as e:
            print(f"Error: {e}")

class Fibonachi(threading.Thread):
    def __init__(self, nombre,numero):
        super().__init__(name=nombre)
        self.numero = numero
    def run(self):
        try:
            if(self.numero == 0):
                print(0)
            elif(self.numero == 1):
                print(1)
            else:
                


if __name__ == "__main__":
    inicio =  time.perf_counter()
    

    
    print("Iniciando Hilos:")
    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()
    fin = time.perf_counter()
    print(f"El programa ha tardado: {fin - inicio}")