import threading
import time


class TareaContador(threading.Thread):
    def run(self):

        time.sleep(2)
            

if __name__ == "__main__":
    hilo = TareaContador()

    print(f"Estado antes de executar: {hilo.is_alive()}")
    hilo.start()

    print(f"Estado durante a execución: {hilo.is_alive()}")

    hilo.join()
    print(f"Estado despois da execución: {hilo.is_alive()}")

