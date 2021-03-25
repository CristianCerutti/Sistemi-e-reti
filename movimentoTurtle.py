from turtle import*

pen = Turtle()
win = Screen()

lung = 30
pen.home()

def control():
    if (pen.ycor() + lung ) > win.window_height() / 2:                                                                  #coordinata y positiva
        return 1
    elif (pen.ycor() - lung) < -1 * win.window_height() /2:                                                             #coordinata y negativa
        return 2
    elif (pen.xcor() + lung) > win.window_width() / 2:                                                                  #coordinata x positiva
        return 3
    elif (pen.xcor() - lung) < -1 * win.window_width() / 2:                                                             #coordinata x negativa
        return 4
    elif (pen.ycor() + lung ) > win.window_height() / 2 and (pen.xcor() + lung) > win.window_width() / 2:               #controlla l'angolo in alto a dx
        return 5
    elif ((pen.ycor() - lung) < -1 * win.window_height() /2 and (pen.xcor() + lung) > win.window_width() / 2):          #controlla l'angolo in basso a dx
        return 6
    elif ((pen.ycor() + lung ) > win.window_height() / 2 and (pen.xcor() - lung) < -1 * win.window_width() / 2):        #controlla l'angolo in alto a sx
        return 7
    elif ((pen.ycor() - lung) < -1 * win.window_height() /2 and (pen.xcor() + lung) > win.window_width() / 2):          #controlla l'angolo in basso a sx
        return 8
    else:
        return 0

def avanti():
    if control() != 1 and control() != 5 and control() != 7: 
        pen.setheading(90)
        pen.forward(lung)
        print(control())
    else:
        pass

def indietro():
    if control() != 2 and control() != 6 and control() != 8:
        pen.setheading(270)
        pen.forward(lung)
        print(control())
    else: 
        pass

def destra():
    if control() != 3 and control() != 5 and control() != 6:
        pen.setheading(0)
        pen.forward(lung)
        print(control())
    else:
        pass

def sinistra():
    if control() != 4 and control != 7 and control() != 8:
        pen.setheading(180)
        pen.forward(lung)
        print(control())
    else:
        pass

win.title("my game")
win.bgcolor("white")
win.setup(width = 500, height = 500)         
win.listen()                                   
win.onkey(avanti, "w")
win.onkey(indietro, "s")
win.onkey(destra, "d")
win.onkey(sinistra, "a")

win.mainloop()