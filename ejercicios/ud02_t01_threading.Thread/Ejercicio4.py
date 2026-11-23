import threading

class TareaContador(threading.Thread):
    def __init__(self,nInicio,nFinal, args):
        super().__init__()
        self.nInicio = nInicio
        self.nFinal = nFinal
        self.args = args
    def run(self):
        for i in range(self.nInicio,self.nFinal+1):
            print(f"{self.args} dice: {i}")

if __name__ == "__main__":
    
    hilo1 = TareaContador(args= "Hilo A",nInicio=1,nFinal=10)
    hilo2 = TareaContador(args= "Hilo B",nInicio=20,nFinal=30)
    print("Inicio de la ejecución concurrente")
    hilo1.start()
    hilo2.start()
    hilo1.join()
    hilo2.join()