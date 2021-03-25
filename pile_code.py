#wrapper   deriva da to wrap, avvolgere 
def push_(pila, elemento):
    pila.append(elemento)

def pop_(pila):
    return pila.pop()           #è una cosa diversa da pop_

def main():
    stack = ["a", "b", "c", "d"]
    push_(stack, "z")
    x = pop_(stack)
    print(x)
    print(stack)

if __name__ == "__main__":
    main()


#code

def enqueu(coda, elemento1):
    coda.append(elemento1)  #inserisce gli elementi da destra, e li toglie a sinistra

def dequeue(coda):
    return coda.pop(0)
