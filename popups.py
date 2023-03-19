from tkinter import *
#para los popups necesitamos importarlos individualmente  
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as Colorchooser
from tkinter import filedialog as FileDialog


"""
#Tipos de popups

#Tipo 1 Show Info
def test ():
    MessageBox.showinfo("Felicitaciones!","Recibiste un popups")#recibe dos argumentos, el primero es el titulo, y el otro el mensaje

#Tipo 2 show Warning
def test ():
    MessageBox.showwarning("Alerta!","Recibiste un popups")#recibe dos argumentos, el primero es el titulo, y el otro el mensaje

#Tipo 3 show Error
def test ():
    MessageBox.showerror("Error!","Recibiste un popups")#recibe dos argumentos, el primero es el titulo, y el otro el mensaje
"""

#Metodo para preguntar
#def test ():
#     resultado = MessageBox.askquestion ("Salir", "Esta seguro que desea salir sin guardar?")
#     if resultado == "yes": #NO
#         root.destroy()
    # resultado = MessageBox.askokcancel ("Salir", "Esta seguro que desea sobreescribir?")
    # if resultado:
    #     root.destroy()
    #resultado = MessageBox.askyesno ("Salir", "Esta seguro que desea salir sin guardar?")
    # resultado = MessageBox.askretrycancel ("Reintentar", "No se puede conectar")
    # if resultado:
    #     root.destroy()
    #Colorchooser.askcolor(title="elige un color")
    #print (color)
    

    #para abrir ficheros y confgurar que tipo de fichero
#def test ():
    # ruta = FileDialog.askopenfilename (title="abrir un fichero", initialdir="C:", 
    # filetypes= (("ficheros de texto", "*.txt"),
    # ("Ficheros de texto avanzado", "*.txt2"),
    # ("Todos los ficheros", "*.*")))
    # print (ruta)

def test ():
    fichero = FileDialog.asksaveasfile (title="Guardar un fichero")
    print (fichero)








root = Tk()
root.title ("Laventanita")
root.iconbitmap("hola.ico")
root.config(bd=20, background="aquamarine")

menubar = Menu (root)
root.config (menu = menubar)

filemenu = Menu (menubar, tearoff=0)
editmenu = Menu (menubar, tearoff=0)
helpmenu = Menu (menubar, tearoff=0)

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



Button (root, text= "Click on me", command=test).pack ()




root.mainloop()





