from tkinter import *

def seleccionar ():
    cadena = ""
    if (leche.get()):
        cadena += "Con leche "
    else:
        cadena += "Sin leche "
    if (azucar.get()):
        cadena += "Con azucar "
    else:
        cadena += "Sin azucar "
    if (edulcorante.get ()):
        cadena += "con edulcorante "
    else:
        cadena+= "Sin edulcorante "
        
    monitor.config (text = cadena)


root = Tk ()

root.title ("Cafeteria")
root.iconbitmap("hola.ico")
root.config(bd=15)


leche = IntVar () #1 si, 0 no
azucar= IntVar () #1 si, 0 no
edulcorante = IntVar () #1 si, 0 no


imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack(side="left")


frame = Frame (root)
frame.pack(side="left")

Label (root, text="Como quieres el cafe?").pack (anchor="w")

Checkbutton (root, text="Con azucar", variable=azucar, onvalue= 1, offvalue=0, command= seleccionar).pack()
Checkbutton (root, text="Con leche", variable= leche, onvalue= 1, offvalue=0, command= seleccionar).pack()
Checkbutton (root, text="Con edulcorante", variable= edulcorante, onvalue= 1, offvalue=0, command= seleccionar).pack()

monitor = Label(frame)
monitor.pack()












root.mainloop()