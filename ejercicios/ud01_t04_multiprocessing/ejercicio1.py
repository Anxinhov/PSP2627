import multiprocessing
result = []
contador = 0
def lista(mylist):
    global contador
    global result
    for idx in mylist:
        contador += 1
        result.append(contador)
    print("Resultado (en p1): {}".format(result[:]))

def lista_productos(mylist):
    global result
    global contador
    for idx in mylist:
        contador+=1
        result.append(contador*2)

    print("Resultado (en p2): {}".format(result[:]))

if __name__ == "__main__":
    
    mylist = multiprocessing.Array("i",10)
    
    p1 = multiprocessing.Process(target=lista, args=(mylist,))
    p2 = multiprocessing.Process(target=lista_productos, args=(mylist,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    