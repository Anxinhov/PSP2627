import threading
contador = 0
class TareaContador(threading.Thread):
    def __init__(self, args):
        super().__init__()
        self.args = args
    def run(self):
        global contador
        for i in range(10):
            contador+=1
            print(f"{contador}:{ self.args}", end=" ")

if __name__ == "__main__":
    
    hilo1 = TareaContador(args= "Si")
    hilo2 = TareaContador(args= "No")
    print("Inicio de la ejecución concurrente")
    hilo1.start()
    hilo2.start()
    hilo1.join()
    hilo2.join()