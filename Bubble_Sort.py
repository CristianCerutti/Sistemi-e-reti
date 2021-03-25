n = int(input("Inserire la grandezza della lista: \n"))
lista = [0] * n             #moltiplichi il contenuto della lista n volte
c = 0
d = 0
swap = 0
for c in range(0, n):
    lista[c] = (input("inserire un valore: \n"))
for c in range(0, n-1):
    for d in range(0,n-c-1):
         if (lista[d] > lista[d+1]):
            lista[d], lista[d+1] = lista[d+1], lista[d]     #per scambiare
print(f"la lista in ordine è: {lista}")
