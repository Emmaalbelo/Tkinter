from tkinter import *

def New ():
    mensaje.set ("New file")

def Open ():
    mensaje.set ("Open file")


def Save ():
    mensaje.set ("Save file")


def Saveas ():
    mensaje.set ("Save file as")




root = Tk ()
root.title ("Editor de texto")



menubar = Menu(root)

filemenu = Menu(menubar, tearoff= 0) 
filemenu.add_command (label= "New", command=New)
filemenu.add_command (label= "Open", command=Open)
filemenu.add_command (label= "Save", command=Save)
filemenu.add_command (label= "Save as...", command=Saveas)
filemenu.add_separator()
filemenu.add_command (label= "Exit", command= root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")

# Caja de texto central

texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0,padx=6,pady=4,font=("Consola",15))

# Monitor inferior 
mensaje = StringVar()
mensaje.set("Bienvenido a tu editor")
monitor = Label(root, textvar= mensaje, justify="left")
monitor.pack(side="left")


#tenemos que a;adir al root el menu bar
root.config(menu= menubar)
















root.mainloop ()