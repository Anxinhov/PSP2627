import multiprocessing 
import time
import random

def rellenar(miArray, q, cola_tiene_algo):
    for num in range(0,5):
        miArray[num] = num + 1
        q.put(num+1)
        cola_tiene_algo.set()
        time.sleep(random.uniform(0,0.3))
    print("Mi array llno: {}".format(list(miArray)))

def sumar(q, cola_tiene_algo):
    suma = 0
    cola_tiene_algo.wait()
    while not q.empty():
        suma += q.get()
        print(suma)
        time.sleep(random.uniform(0,0.3))
    print("Resultado final: {}".format(suma))

if __name__ == '__main__':
    miArray =multiprocessing.Array('i',5)

    q = multiprocessing.Queue()

    cola_tiene_algo = multiprocessing.Event()

    p1 = multiprocessing.Process(target=rellenar, args=(miArray, q, cola_tiene_algo))
    p2 = multiprocessing.Process(target=sumar, args=(q, cola_tiene_algo))

    p1.start()
    p2.start()
    p1.join()
    p2.join()