from tkinter import *

#Raiz
root = Tk ()

#para dar titulo A LA VENTANA
root.title ("Hola mundo")

#para cambiarle el tamaño a la ventana
#si le decimos FALSE, FALSE, sig que la ventana
#no se puede redimencionar 
#TRUE, FALSE (ANCHO SI, NO EN ALTURA)
#FALSE, TRUE, (NO EN ANCHO, SI EN ALTURA)
#TRUE, TRUE, DIMENCIONAR LIBRE
root.resizable()

#para ponerle un icono a la ventana.
#en este caso usamos el del curso
root.iconbitmap("hola.ico")

#FRAME / MARCO
#para crear un marco para darle tamaño a la ventana
#Siempre tiene un tamaño estandar, con esto podemos configurar
#para ponerle las dimensiones que queramos. 
#marco = marco (enmarca a la raiz, osea al programa, por eso que de 
# parametro, ponemos root)
frame = Frame (root, width=480, height=320)
#Frame.pack()
#con pack podemos configurar donde se mantendra el marco
#por defecto aparece centrado arriba. pero podemos 
#configurar por medio del parametro side= "right" 
#side= "botton" y por el parametro anchor= e,o,n,s
#Frame.pack(side="botton", anchor="w")
#Frame.pack(fill="x", expand=1)
#Frame.pack(fill="y", expand=1)

#para que se expanda a todos los extremos
#            ambos (eje x y) expand 1 (TRUE)
frame.pack(fill="both", expand=1)


#con config, se configura espesificamente el tamaño
#Frame.config(width=480, height=320)
#a la altura y ancho lo podemos configurar en la llamada
#al marco directamente
#Frame = Frame (root, width=480, height=320)

#una boludes, para cambiar el cursor. solo aplica al tamaño que configuramos
frame.config(cursor="pirate")

#PARA CAMBIAR EL COLOR DEL FONDO
frame.config(bg="lightblue")

#PARA CAMBIAR EL TIPO DE BORDE
frame.config(relief= "sunken")

#TAMAñO DE BORDE
frame.config(bd=25)



#PODEMOS USAR LAS MISMAS CONFIGURACIONES DIRECTAMENTE
#PARA EL ROOT
root.config(cursor="arrow")
root.config(bg="blue")
root.config(relief= "ridge")
root.config(bd=15)



#con Mainlopp llamamos a la ventana (creamos
# el recuadro)
root.mainloop()

