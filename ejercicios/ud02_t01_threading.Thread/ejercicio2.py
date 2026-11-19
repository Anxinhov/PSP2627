import threading


class TareaA(threading.Thread):
    def run(self):
        for i in range(30):
            print("NO", end=" ")
        print("")

class TareaB(threading.Thread):
    def run(self):
        for i in range(30):
            print("YES", end=" ")
        print("")

if __name__ == "__main__":
    hiloA = TareaA()
    hiloB = TareaB()

    print("Ejecucion en hilo A")
    hiloA.start()

    print("Ejecucion en hilo B")
    hiloB.start()

    print("Ejecucion en main")

    hiloA.join()
    hiloB.join()