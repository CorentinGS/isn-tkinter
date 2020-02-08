from tkinter import *

myWindow = Tk()

x = 0
y = 0
l = 0
c = 0


# Fonctions
def create_grid():
    grille.delete("all")
    for i in range(5, 305, 20):
        grille.create_line([(i, 5), (i, 305)])

    for i in range(5, 305, 20):
        grille.create_line([(5, i), (305, i)])

    grille.create_line([(5, 5), (5, 305)])
    grille.create_line([(305, 5), (305, 305)])
    grille.create_line([(5, 5), (305, 5)])
    grille.create_line([(5, 305), (305, 305)])


def get_coord(event):
    global x, y
    x = event.x
    y = event.y
    result_labelx.config(text=f"abscisse : {x}")
    result_labely.config(text=f"ordonnée : {y}")
    ligne = int(y / 20) + 1
    column = int(x / 20) + 1
    result_colonne.config(text=f"colonne : {column}")
    result_ligne.config(text=f"ligne : {ligne}")

    create_grid()
    grille.create_line([(x - 5, y), (x + 5, y)])
    grille.create_line([(x, y - 5), (x, y + 5)])


# Widgets
result_labelx = Label(myWindow, text=f"abscisse : {x}")
result_labely = Label(myWindow, text=f"ordonnée : {x}")
result_ligne = Label(myWindow, text=f"ligne : {l}")
result_colonne = Label(myWindow, text=f"colonne : {c}")
boutonGrid = Button(myWindow, text="Tracer la grille", command=create_grid)

grille = Canvas(myWindow, width=310, height=310)

# Affichage des Widgets
boutonGrid.grid(row=0, column=1)
result_labelx.grid(row=1, column=1)
result_labely.grid(row=2, column=1)
result_ligne.grid(row=3, column=1)
result_colonne.grid(row=4, column=1)
grille.grid(row=0, column=0, rowspan=5)

# Main
myWindow.bind("<Button 1>", get_coord)
myWindow.mainloop()