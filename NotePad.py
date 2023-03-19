from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog
from io import open

ruta = "" #la utilizaremos de ruta del fichero


def New ():
    #global es para informar a nuestro programa, que la variable es global y no solo de la funcion.
    global ruta
    mensaje.set ("New file")
    ruta = ""
    resultado = MessageBox.askyesno ("Salir", "Esta seguro que desea salir sin guardar?")
    if resultado:
        texto.delete(1.0,"end")
    root.title(ruta + " - Mi editor")

def Open ():
    global ruta
    mensaje.set ("Open file")
    ruta = FileDialog.askopenfilename (title="abrir un fichero", initialdir=".", 
    filetypes= (("ficheros de texto", "*.txt"),))
    
    if ruta != "":
        fichero = open (ruta, "r")#r para indicar que es solo lectura. Read
        contenido = fichero.read ()
        texto.delete(1.0, "end")#para borrar el contenido. desde la posicion 0 hasta el final
        texto.insert ("insert", contenido)
        fichero.close()
        root.title(ruta + " - Mi editor")

def Save ():
    global ruta
    mensaje.set ("Save file")
    if ruta != "":
        contenido = texto.get (1.0, "end-1c")#recupere todo menos el ultimo caracter que es un salto de linea
        fichero = open (ruta, "w+")#w+ escritura mas lectura
        fichero.write (contenido)
        fichero.close()
        mensaje.set ("Fichero guardado correctamente")
    else: Saveas ()


def Saveas ():
    global ruta
    mensaje.set ("Save file as")
    fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode = "w", defaultextension= "*.txt",filetypes= (("ficheros de texto", "*.txt"),))
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get (1.0, "end-1c")#recupere todo menos el ultimo caracter que es un salto de linea
        fichero = open (ruta, "w+")#w+ escritura mas lectura
        fichero.write (contenido)
        fichero.close()
        mensaje.set ("Fichero guardado correctamente")
    else:
        mensaje.set ("Guardado cancelado")
        ruta = ""


def Exit ():
    resultado = MessageBox.askquestion ("Salir", "Esta seguro que desea salir sin guardar?")
    if resultado == "yes": #NO
        root.quit()
    else:
        Saveas()


root = Tk ()
root.title ("Editor de texto")



menubar = Menu(root)

filemenu = Menu(menubar, tearoff= 0) 
filemenu.add_command (label= "New", command=New)
filemenu.add_command (label= "Open", command=Open)
filemenu.add_command (label= "Save", command=Save)
filemenu.add_command (label= "Save as...", command=Saveas)
filemenu.add_separator()
filemenu.add_command (label= "Exit", command= Exit)
menubar.add_cascade(menu=filemenu, label="File")




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