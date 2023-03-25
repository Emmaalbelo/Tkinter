
from tkinter import *

root = Tk ()
root.title ("Hola mundo")
root.iconbitmap ("hola.ico")

'''
frame = Frame(root)
frame.pack()

#configurar campos de texto editable para el usuario
entry = Entry (root)
entry.pack(side="right")

label = Label(root, text="Nombre")
label.pack(side="left")
#SI AGREGAMOS MAS, SE VERA PARA EL CULO
entry2 = Entry (root)
entry2.pack(side="right")

label2 = Label(root, text="Apellido")
label2.pack(side="left")

#ASI SI SE VERIA MEJOR PERO NO DEL todo
entry = Entry (frame)
entry.pack(side="right")

label = Label(frame, text="Nombre")
label.pack(side="left")


frame2 = Frame(root)
frame2.pack()

entry2 = Entry (frame2)
entry2.pack(side="right")

label2 = Label(frame2, text="Apellido")
label2.pack(side="left")
'''
#METODO GRID / GRILLA, sirve para configurar todo en una grilla mediante
#columnas y fila (column , row)

label = Label(root, text="Nombre")
label.grid(row= 0, column= 0, sticky="e", padx=5,pady=5)#formato sticky para pegar
#padx=5,pady=5 para configurar un espacio entre las celdas
entry = Entry (root)
entry.grid(row= 0, column= 1, padx=5,pady=5)
#entry.config (justify="right")la escritura a la derecha
#entry.config (state="disable""normal")

label2 = Label(root, text="Apellido")
label2.grid(row= 1, column= 0, sticky= "w", padx=5,pady=5)  

entry2 = Entry (root)
entry2.grid(row= 1, column= 1, padx=5,pady=5)
#entry.config (justify="center")
#entry.config (show="*" ) apareceran * en lugar de lo que escribimos 
#sirve para los campos de contraseñas

root.mainloop ()