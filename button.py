from tkinter import *
#pack () sirve para que lo que estamos programando se muestre en la pantalla

def sumar ():
    resultado.set (float(n1.get())+ float(n2.get()))
    borrar()

def resta ():
    resultado.set (float(n1.get())- float(n2.get()))
    borrar()

def producto ():
    resultado.set (float(n1.get())* float(n2.get()))
    borrar()


def borrar ():
    n1.set("")
    n2.set("")

root = Tk()
root.config(bd=15)

root.title ("Hola PIPI")
root.iconbitmap("hola.ico")
root.config (background= "aquamarine",)

frame = Frame(root)
frame.config(background= "black")

n1 = StringVar()
n2 = StringVar()
resultado = StringVar()

Label (root, text="Numero 1", background= "aquamarine").pack()
Entry (root, justify= "center", textvariable= n1).pack()#primer numero
Label (root, text="Numero 2", background= "aquamarine").pack()
Entry (root, justify= "center", textvariable= n2).pack()#segundo numero


Label (root, text="\nResultado", background= "aquamarine").pack()
#                                                      desactivamos para que no se pueda editar el resultado
Entry (root, justify= "center", textvariable= resultado, state="disable").pack()#resultado

Label (root, text="", background= "aquamarine").pack()
#para crear un boton
#con comand le atribuimos una funsion al boton
Button(root, text="Sumar", command= sumar).pack(side="left")
Button(root, text="resta", command= resta).pack(side="left")
Button(root, text="producto", command= producto).pack(side="left")




root.mainloop()