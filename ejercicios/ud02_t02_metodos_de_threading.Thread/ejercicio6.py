import threading
import time

class Factorial(threading.Thread):
    def __init__(self,numero):
            super().__init__()
            self.numero = numero
    
    def run(self):
            try:
                print(f"empieza el proceso … cálculo del factorial de: {self.numero}")
                if(self.numero == 0):
                    print(f"El factorial de {self.numero} es 1")
                else:
                    i = 1
                    for l in range(1,self.numero +1):
                        i *= l
                    print(f"acabó el proceso ….. el factorial de: {self.numero} es {i}")
            except Exception as e:
                        print(f"Error: {e}")
if __name__ == "__main__":
    inicio =  time.perf_counter()
    hilo1 = Factorial(numero=5)
    hilo2 = Factorial(numero=6)
    hilo3 = Factorial(numero=7)
    hilo4 = Factorial(numero=8)
    hilo5 = Factorial(numero=9)
    
    print("Iniciando Hilos:")
    hilo1.start()
    hilo2.start()
    hilo3.start()
    hilo4.start()
    hilo5.start()

    
    hilo1.join()
    hilo2.join()
    hilo3.join()
    hilo4.join()
    hilo5.join()
    fin = time.perf_counter()
    print(f"El programa ha tardado: {fin - inicio} segundos")