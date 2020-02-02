from tkinter import *

myWindow = Tk()

x = 0
y = 0
l = 0
c = 0
result_labelx = Label(myWindow, text=f"abscisse : {x}")
result_labely = Label(myWindow, text=f"ordonnée : {x}")
result_ligne = Label(myWindow, text=f"ligne : {l}")
result_colonne = Label(myWindow, text=f"colonne : {c}")
grille = Canvas(myWindow, width=300, height=300)


def create_grid():
    for i in range(0, 300, 20):
        grille.create_line([(i, 0), (i, 300)])

    for i in range(0, 300, 20):
        grille.create_line([(0, i), (300, i)])


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

boutonGrid = Button(myWindow, text="Tracer la grille", command=create_grid)

boutonGrid.grid(row=0, column=1)
result_labelx.grid(row=1, column=1)
result_labely.grid(row=2, column=1)
result_ligne.grid(row=3, column=1)
result_colonne.grid(row=4, column=1)
grille.grid(row=0, column=0, rowspan=5)
myWindow.bind("<Button 1>", get_coord)

myWindow.mainloop()
