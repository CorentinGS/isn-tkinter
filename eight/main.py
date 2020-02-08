from tkinter import *

root = Tk()
root.geometry("300x300")


# Fonctions
def quitter():
    root.quit()
    root.destroy()


def left(event):
    x1, y1, x2, y2 = draw.coords(ball)
    draw.coords(ball, x1 - 5, y1, x2 - 5, y2)


def right(event):
    x1, y1, x2, y2 = draw.coords(ball)
    draw.coords(ball, x1 + 5, y1, x2 + 5, y2)


def up(event):
    x1, y1, x2, y2 = draw.coords(ball)
    draw.coords(ball, x1, y1 - 5, x2, y2 - 5)


def down(event):
    x1, y1, x2, y2 = draw.coords(ball)
    draw.coords(ball, x1, y1 + 5, x2, y2 + 5)


# Widgets
draw = Canvas(root)
boutonQuitter = Button(root, text='Quitter', command=quitter)

# Affichage des Widgets
draw.pack()
boutonQuitter.pack()

# Main
ball = draw.create_oval(100, 100, 150, 150, fill='red')
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
root.mainloop()
