import pygame   #installata da noi
import sys  #nativa = preinstallata
DIMENSIONI = (300, 250)
NERO = (0,0,0)
BIANCO = (255, 255, 255)
ROSSO = (255, 0 ,0)
finestra = pygame.display.set_mode(DIMENSIONI)
Pavimento = [[1,1,0,0,0,0], [0,0,0,0,1,0], [1,0,1,0,0,0], [0,0,1,0,0,0]]
NRIGHE = len(Pavimento)
NCOLONNE = len(Pavimento[0])

def drawgrid():
    dimensione = 50
    dimensionex = DIMENSIONI[0]//NCOLONNE       #// divisione senza resto
    dimensioney = DIMENSIONI[1]//NRIGHE
    conty = 0
    for x in range(0, DIMENSIONI[0], dimensioney):
        riga = conty

        if (conty<NRIGHE-1):
            conty += 1
        contx = 0
        for y in range(0, DIMENSIONI[0], dimensionex):
            colonna = riga[contx]

            if (contx<NCOLONNE-1):
                contx +=1
            if colonna == 0:
                piastrella = pygame.Rect(x,y,dimensionex, dimensioney)
                pygame.draw.rect(finestra, BIANCO, piastrella, 1)

def main():
    pygame.init()   
    finestra.fill(NERO)
    while True:
        drawgrid()
        for event in pygame.event.get():        #per fermare il gioco
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()      #per fermare il programma
        pygame.display.update()


if __name__ == "__main__":
    main()

    #x = random.random()
           # if x<PROBABILITA_OSTACOLO:
             #   riga.append(1)
            #else:
            #    riga.append(0)  genera con il 20% delle volte 0 o 1