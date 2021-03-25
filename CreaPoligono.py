#per aggiungere le librerie si schive import {nome libreria}
import turtle               #importa la libreria turtle e tutto ciò che contiene
#from turtle import *        #importa tutte le classi e si possono usare direttamente col loro nome

nlati = int(input("inserire il numero dei lati: \n"))
alice = turtle.Turtle()
alice.begin_fill()
cont = nlati
while(cont > 0):
    alice.forward(40)
    alice.left(360/nlati)
    cont = cont-1
alice.end_fill()
alice.done()