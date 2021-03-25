numero = 7 #è un oggetto ovvero un istanza della classe int
#esempio di f-string
print(f"il valore di numero è {numero}")
#esempio di concatenazione di stringe
print("il valore di numero è "+str(numero))

s1 = 'Ciao'
s2 = "un'altra stringa"

print(s1 == s2)
#python è un linguaggio orientato agli oggetti in python tutto è un oggetto
#COLLEZIONI: liste, tuple, dizionari

#LISTE: sono "simili" agli array del c

lista = [3,5,1,6,7]
print(f"la lista è: {lista}")

#FUNZIONI
def lamiafunzione(argomento1, argomento2):
    #codice della funzione indentato
    return argomento1

print(lamiafunzione)

#PYTHON STYLE :)
for elemento in lista: 
    print(elemento)

#c sTyLe :(
lunghezza = len(lista)
for indice in range(0, lunghezza):
    print(lista[indice])
    print(f"indice: {indice} - elemento{lista[indice]}")

for indice, elemento in enumerate(lista):    #scorre due indici
    print(f"indice : {indice} - elemento: {lista[indice]}")

#inserire valori dell'utente caricati su una lista (primo modo)

lista1 = []   #si crea una lista vuota
valore = 0
while (int(valore)!=-1):
    valore = input("inserisci un valore: ")   #fa una fusione tra printf e scanf
    lista.append(int(valore))           #si usa il punto perché la lista è un oggetto
print(lista)

#         0   1   2   3  4  5  6   7
lista = [ 23, 43, 12, 1, 5, 6, 12, -1]
#         -8  -7  -6  -5 -4 -3 -2  -1
#slicing di liste

print(lista[4])  #estrae un elemento
print(lista[2:5]) #tampa gli elementi dalla 2 (incluso) fino a 5 (escluso)
print(lista[-2])  #penultimo elemento
print(lista[0:-1])  

stringa = "Itis Delpozzo"
print(stringa[0:5])   #stampa solo itis perché le stringhe sono liste di caratteri
print(stringa.startswith("Itis"))  #controlla se la stringa inizia con "Itis" e restituisce un buleano del risulato

#python style
for elemento in lista:
    print(elemento)     #stampa tutti gli elementi della lista
i = 0
##python style con enumerate
for i, elemento in enumerate(lista):
    print(f"{i} - {elemento}")          

#while 
counter = 0
while(counter < len(lista)):
    print(lista[counter])
    counter = counter + 1


#i dizionari
#un dizionario una collezione di elementi, ciascuono dei quali è costituito da una chiave e un valore
#collezione non ordinata
#ogni lemento ha una chiave e un valore (chiave: 1; valore: antonelli)
dizionario = {1: "antonelli", 2: "becchis", 3: "bianco", 4: "bongiovanni"}
#per accedere al valore di un elemento del dizionario  si utilizza la notazione
#nome_dizionario[chiave]
dizionario[19] = "orlando"
print(dizionario)

#canzone = {"numero": 1, "titolo": "francesco", }

file = open("./instagram.csv", "r")
for riga in file:
    print(riga, end="")         #end si mette se no stampa con un a capo in più, che di per se è comodo
file.close()

segments = "ciao"
print(f"{len(segments)-1,0,-1}")


#DIZIONARI DI FUNIONI

def somma(a,b):
    return a+b
def moltiplicazione(a,b):
    return a*b


dizionario_funzioni = {0: somma, 1: moltiplicazione}   #il valore python lo vede come puntatore alla funzione interessata
def main():
    val_utente = int(input("0 per sommare, 1 per moltiplicare: "))
    a = int(input("primo numero"))
    b = int(input("secondo numero")) 
    try:   
        x = dizionario_funzioni[val_utente] (a,b)           #dizionario alla posizione [] e la funzione vuole i parametri a e b
    except:
        print("hai inserito un valore errato")

#PARAMETRI DI DEFAULT IN INPUT ALLE FUNZIONI

def fun(lista_numeri, stampa = False):
    lista_quadrati = [x*x for x in lista_numeri]   #compressione di liste
    if stampa:
        print(lista_quadrati)
    #lista_quadati = []
    #for(x in lista_numeri):
    #    lista_quadrati.append(x*x)

    return lista_quadrati
fun([1,2,3,4], True)








if __name__ == "__main__":
    main() 



