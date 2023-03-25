#Tkinter tutorial

import tkinter as tk

#Para crear una ventana. La podemos llamar root o window
root = tk.Tk()
#Para ver la ventana creada tenemos que llamar a mainloop
#root.mainloop() 

#Al tamano de la ventana lo configuramos desde:
root.geometry('500x500')

#para ponerle titulo a la venta (no al programa, si no a la ventana)
root.title("My first GUI")

#para ponerle titulo a la aplicacion 
label = tk.Label(root, text="Hello world!", font=('Arial', 18))
label.pack(pady=20, padx=20)
#Las coordenadas de donde aparece el texto las modificamos 
#por medio de PADY= y PAX= (ejes X Y)

#Para crear una caja de texto
texbox = tk.Text(root, height=1, font=('Arial', 16))
texbox.pack(padx=10)
#El tama;o por medio de heigth= width=
#para ver los otros parametros, Text: go to definition

#Para crear varios botones alineados por columnas y lineas. 
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

#Para configurar cada boton de "buttonframe". 
#"buttonframe" pasa a ser el master en lugar de root
#por que estamos modificando algo directamente de "buttonframe"
btn1 = tk.Button(buttonframe,text='1', font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E) #W= west E=East
#El comando sticky es para que se pegue a los bordes de la ventana
btn2 = tk.Button(buttonframe,text='2', font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
btn3 = tk.Button(buttonframe,text='3', font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')
#el comando fill es para extirar los botos a la coordenada indicada

anotherbutton = tk.Button(root, text='Hola')
anotherbutton.place(x=200, y=200, height=100, width=100)
#el comando place es para la coordenada indicada

#Para entradas de texto (por ejemplo, para dejar comentarios)
myentry = tk.Entry(root)
myentry.pack()

#para crear un boton
button = tk.Button (root, text="Clik me!", font=('Arial', 18))


root.mainloop() 
#Para ver la ventana creada tenemos que llamar a mainloop
#root.mainloop()