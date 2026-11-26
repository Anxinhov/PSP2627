import threading
import time



class Factorial(threading.Thread):
    def __init__(self,numero):
            super().__init__()
            self.numero = numero
    
    def run(self):
            try:
                if(self.numero == 0):
                    print(f"El factorial de {self.numero} es 1")
                else:
                    i = 1
                    for l in range(1,self.numero +1):
                        i *= l
                    print(f"El factorial de {self.numero} es {i}")
            except Exception as e:
                        print(f"Error: {e}")

class Fibonacci(threading.Thread):
    def __init__(self,numero):
        super().__init__()
        self.numero = numero
    def run(self):
        try:
            if(self.numero == 0):
                print(f"El fibonacci de {self.numero} es 0")
            elif(self.numero == 1):
                print(f"El fibonacci de {self.numero} es 1")
            else:
                n = 0
                n2 = 1
                for i in range(1,self.numero):
                    n3 = n2
                    n2 = n + n2
                    n = n3
                print(f"El fibonacci de {self.numero} es {n2}")
        except Exception as e:
                    print(f"Error: {e}")
        


if __name__ == "__main__":
    inicio =  time.perf_counter()
    hilo1 = Factorial(numero=6)
    hilo2 = Fibonacci(numero=6)
    
    print("Iniciando Hilos:")
    hilo1.start()
    hilo2.start()

    
    hilo1.join()
    hilo2.join()
    fin = time.perf_counter()
    print(f"El programa ha tardado: {fin - inicio} segundos")