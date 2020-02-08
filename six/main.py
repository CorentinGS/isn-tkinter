from random import *
from tkinter import *

myWindow = Tk()
couleurs = ['red', 'purple', 'pink', "green", 'yellow']
old_couleur = " "
nbr = 0
total = 0
couleur = "red"
ratios = []


# Fonctions
def change():
    global couleur
    global old_couleur
    couleur = choice(couleurs)
    if old_couleur == couleur:
        change()
    else:
        old_couleur = couleur
        colorLabel.config(text=f"Couleur actuelle : {couleur}")
        colorDisplayer.config(bg=couleur)


def rectangle():
    global moyen_long, moyen_larg, nbr, couleur, ratios, total

    x1 = randint(0, 400)
    x2 = randint(0, 400)
    y1 = randint(0, 400)
    y2 = randint(0, 400)
    dessin.create_rectangle(x1, y1, x2, y2, fill=couleur)
    len_x = abs(x2 - x1)
    len_y = abs(y2 - y1)
    total += 1
    if len_x > len_y:
        ratios.append(len_x / len_y)
    else:
        ratios.append(len_y / len_x)
    moyenne = round(sum(ratios) / total, 2)
    ratioLabel.config(text=f"Ratio : {moyenne}")
    if couleur == "red":
        nbr += 1
        numberLabel.config(text=f"Nombre de rectangle : {nbr}")


def circle():
    r = randint(0, 50)
    x = randint(50, 350)
    y = randint(50, 350)
    x1 = x - r
    x2 = x + r
    y1 = y - r
    y2 = y + r
    dessin.create_oval(x1, y1, x2, y2, fill=couleur)


# Widgets
boutonChange = Button(myWindow, text="Changer de couleur", command=change)
boutonRectangle = Button(myWindow, text='Nouveau rectangle', command=rectangle)
boutonCercle = Button(myWindow, text='Nouveau cercle', command=circle)
dessin = Canvas(myWindow, width=400, height=400)
numberLabel = Label(myWindow, text=f"Nombre de rectangle : {nbr}")
colorLabel = Label(myWindow, text=f"Couleur actuelle : {couleur}")
colorDisplayer = Label(myWindow, width=4, height=2, bg=couleur)
ratioLabel = Label(myWindow, text=f"Ratio : {0}")

# Affichage des Widgets
dessin.grid(row=0, column=0, rowspan=8)

boutonChange.grid(row=0, column=1)
boutonRectangle.grid(row=1, column=1)
boutonCercle.grid(row=2, column=1)

numberLabel.grid(row=3, column=1)
colorLabel.grid(row=4, column=1)
colorDisplayer.grid(row=5, column=1)
ratioLabel.grid(row=6, column=1)

# MainLoop
change()
myWindow.mainloop()
