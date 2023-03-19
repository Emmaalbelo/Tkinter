from tkinter import *

root = Tk()

root.title("Hola mundo")
root.iconbitmap("hola.ico")

texto= Text(root)

texto.pack()
texto.config(width= 30,height=10 )#no es por pixeles, si no por caracteres

texto.config (font=("consolas", 12), padx=5 , pady=5, selectbackground= "red")



root.mainloop()