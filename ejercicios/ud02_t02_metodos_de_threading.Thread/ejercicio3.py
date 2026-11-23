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
    hilo1 = TareaContador(args= "Hilo A")
    
    print("Iniciando Hilo secundario:")
    hilo1.start()
    hilo1.join()
    fin = time.time()
    print(f"El proceso ha tardado: {fin - inicio}")
    