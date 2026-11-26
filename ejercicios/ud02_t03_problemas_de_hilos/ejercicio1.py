import threading
import time

saldo_actual = 2000
lock = threading.Lock()

def retirar(cantidad, nombre):
    global saldo_actual
    for _ in range(cantidad):
        lock.acquire()
        try:
            temp = saldo_actual
            temp -= cantidad
            time.sleep(0.001)
            saldo_actual = temp
        finally:
            lock.release()

if __name__ == "__main__":
    hilos = [threading.Thread(target=retirar, args=(300,"Yo")) for _ in range(5)]
    hilos2 = [threading.Thread(target=retirar, args=(100, "Cónyuge")) for _ in range(5)]
    for h in hilos: h.start()
    for h in hilos2: h.start()
    for h in hilos: h.join()
    for h in hilos2: h.join()
    print("Valor final (acquire/release):", saldo_actual)

