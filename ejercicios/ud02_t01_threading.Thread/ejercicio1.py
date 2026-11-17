import threading


class TareaContador(threading.Thread):
    def run(self):
        for i in range(30):
            print("NO", end=" ")
            

if __name__ == "__main__":
    hilo = TareaContador()

    print("[Principal] Iniciando hilo contador...")
    hilo.start()

    for i in range(30):
        print("YES", end=" ")

    hilo.join()
    print("[Principal] El hilo contador ha terminado.")

