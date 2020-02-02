from random import *
from tkinter import *

myWindow = Tk()
couleurs = ['red', 'purple', 'pink', 'yellow']


def change():
    global couleur
    couleur = choice(couleurs)


def rectangle():
    change()
    x1 = randint(0, 400)
    x2 = randint(0, 400)
    y1 = randint(0, 400)
    y2 = randint(0, 400)
    dessin.create_rectangle(x1, y1, x2, y2, fill=couleur)


boutonChange = Button(myWindow, text="Changer de couleur", command=change)
boutonRectangle = Button(myWindow, text='Nouveau rectangle', command=rectangle)
dessin = Canvas(myWindow, width=400, height=400)

boutonChange.grid(row=0, column=1)
boutonRectangle.grid(row=1, column=1)
dessin.grid(row=0, column=0, rowspan=6)

myWindow.mainloop()
