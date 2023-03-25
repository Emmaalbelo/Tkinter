from tkinter import*


def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
#funcion para recuperar el valor a la hora de marcar una opcion

def reset():
    opcion.set (None)
    monitor.config(text="")

root = Tk()

root.title ("La ventanita")
root.iconbitmap("hola.ico")

#para darle funcionalidad al boton debemos crear una variable para asignarle
opcion = IntVar()


#para agregar un boton redondo para tildar.
Radiobutton(root, text= "Opcion 1",variable= opcion, value=1, command= seleccionar).pack()
Radiobutton(root, text= "Opcion 2",variable= opcion, value=2, command= seleccionar).pack()
Radiobutton(root, text= "Opcion 3",variable= opcion, value=3, command= seleccionar).pack()

monitor = Label(root)
monitor.pack ()

Button (root,text="Reiniciar", command=reset).pack()

root.mainloop()