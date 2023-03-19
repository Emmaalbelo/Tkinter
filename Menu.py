from tkinter import *

root = Tk()

root.title("La ventanita")
root.iconbitmap("hola.ico")
root.config(bd=20,background="aquamarine")

#el menu no se empaqueta (.pack()) si no que hay que agregarlo a la raiz (root)
#de manera manual
menubar = Menu (root)
root.config(menu= menubar)

#creamos las variables que contiene el menu
filemenu = Menu(menubar, tearoff= 0) 
#Agregamos elementos (sub comandos) a las opciones de menu
filemenu.add_command (label="New")
filemenu.add_command (label="Open")
filemenu.add_command (label="Save")
filemenu.add_command (label="Close")
filemenu.add_separator()
filemenu.add_command (label= "Out", command= root.quit)#para cerrar el programa 

editmenu = Menu(menubar, tearoff= 0)
editmenu.add_command (label= "Cut")
editmenu.add_command (label= "Copy")
editmenu.add_command (label= "Paste")



helpmenu = Menu(menubar, tearoff= 0)
helpmenu.add_command (label= "Help")
helpmenu.add_separator()
helpmenu.add_command (label= "About")

#creamos el contenido del menu (la barra con nombres)
menubar.add_cascade (label= "File", menu= filemenu)
menubar.add_cascade (label= "Edit", menu= editmenu)
menubar.add_cascade (label= "Help", menu= helpmenu)










root.mainloop()