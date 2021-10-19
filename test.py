import os
from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk

fenetre = tk.Tk()
fenetre.withdraw

label = Label(fenetre, text="V'Sender")
label.pack()

def file_path():
    global path
    path = filedialog.askopenfilename()
    print(path)
    avatar.set("{}".format(path))



avatar = tk.StringVar()
avatar.set("Avatar Path")
fieldd2 = tk.Entry(fenetre, textvariable=avatar, width=50)
fieldd2.pack()

booton = Button(text ="Choose a avatar file", command=file_path)
booton.pack()

fenetre.mainloop()