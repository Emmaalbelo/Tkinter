#Label = etiqueta de texto
#https://www.udemy.com/course/python-3-al-completo-desde-cero/learn/lecture/5369894#search

from tkinter import *

root = Tk()

#Variables dinamicas
texto = StringVar()
texto.set ("Un nuevo texto")

# frame = Frame (root, width= 480, height= 320)
# frame.pack ()

root.title ("Hola mundo")
root.iconbitmap("hola.ico")

#label = Label(root, text="Hola mundo")
#place / lugar, es para configurar el lugar especifico donde 
# aparecera el texto, atravez de coordenadas x y
#label.place (x= 0, y=0)

#Podemos en lugar de hacer un place, un pack
#label.pack ()

#truco para crear varias etiquetas empaquetadas Pack
#Usamos .pack()
Label(root, text="Hola mundo").pack (anchor= "nw")
label = Label(root, text="otra etiqueta")
label.pack (anchor= "center")
Label(root, text="Y una mas").pack (anchor= "se")


#Podemos cambiar alguna configuracion. Siempre que tengamos asignado
#label a una variable
#color de fondo
label.config (bg="green")

#color de las letras 
label.config (fg="blue")

#Fuente y tamaño de las letras 
label.config (font=("verdana",20))


label.config (textvariable=texto)

#Todas estas configuraciones podemos ponerla en una sola config
#label.config (bg="green", fg="blue", font=("verdana",20))


#Para agregar una imagen al label
imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack()


















root.mainloop()