def push_(pila, elemento):
    pila.append(elemento)

def pop_(pila):
    return pila.pop()       

def main():
    stringa = input("inserire una stringa di parentesi: ")
    pila = []
    cont = 0
    pos = 0
    lunghezza = len(stringa)
    for _ in range(lunghezza):
        if(stringa[pos] == '(' ):
            push_(pila, '(')
            cont+=1
        elif(stringa[pos] == '['):
            push_(pila, '[')
            cont+=1
        elif(stringa[pos] == '{'):
            push_(pila, '{')
            cont+=1
        elif(stringa[pos] == ')'):
            push_(pila, ')')
            cont+=1
        elif(stringa[pos] == ']'):
            push_(pila, ']')
            cont+=1
        elif(stringa[pos] == '}'):
            push_(pila, '}')
            cont+=1
        pos += 1
    for _ in range(cont):
        pop_(pila)   


if __name__ == "__main__":
   main()