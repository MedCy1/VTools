import os
from tkinter import * 
from tkinter import messagebox
import requests
from requests.api import get

fenetre = Tk()

label = Label(fenetre, text="V'Sender")
label.pack()




maxchars_uname = 10

ura = StringVar()
ura.set("Write URL here")
urll = Entry(fenetre, textvariable=ura, width=50)
urll.pack()

message = StringVar()
message.set("Write message here")
messagee = Entry(fenetre, textvariable=message, width=50)
messagee.pack()

username = StringVar()
username.set("Write username here")
usernamee = Entry(fenetre, textvariable=username, width=50)
usernamee.pack()



def getURL():
    global link
    link=ura.get()
    #https://discord.com/api/webhooks/898286370693472296/nujOOXcKGvMwFa7VR2-GU8IF84oye2DwXe3f83J9G7W2LZ5TDKHTfqcaxdFpHnRYqbUB


def getUsername():
    global uname
    uname=username.get()


def getMessage():
    global mess
    mess=message.get()


def erreur():
    messagebox.showerror(title="Error", message="There is a error :\n\nEnter a valid webhook URL.")

def envoye():
    messagebox.showinfo(title="Sent !", message="Message sent !")

def vide():
    messagebox.showerror(title="Error", message="There is a error :\n\nThe message cannot be blank.")


def sendWebhook():
    getURL()
    getUsername()
    getMessage()
    liened = "https://"
    try:
        link.index(liened)
    except ValueError:
        erreur()
    else:
        pass

    try:
        if mess == "":
            vide()
    except:
        print("except lol")
    else:
        pass

    data = {
    "content" : mess,
    "username" : uname
    }

    url = link

    result = requests.post(url, json = data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
            print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))
        envoye()

booton = Button(text ="Send !", command=sendWebhook)
booton.pack()


fenetre.mainloop()