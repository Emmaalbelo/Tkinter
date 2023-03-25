from tkinter import *

#Raiz
root = Tk ()
#para dar titulo A LA VENTANA
root.title ("Hola mundo")

#para ponerle un icono a la ventana.
#en este caso usamos el del curso
root.iconbitmap("hola.ico")

#para cambiarle el tamaño a la ventana
#si le decimos FALSE, FALSE, sig que la ventana
#no se puede redimencionar 
#TRUE, FALSE (ANCHO SI, NO EN ALTURA)
#FALSE, TRUE, (NO EN ANCHO, SI EN ALTURA)
#TRUE, TRUE, DIMENCIONAR LIBRE
root.resizable()


#con Mainlopp llamamos a la ventana (creamos
# el recuadro)
root.mainloop()


