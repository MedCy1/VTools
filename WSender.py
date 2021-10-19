import os
from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
import requests
from requests.api import get
from dhooks import Webhook, Embed


fenetre = tk.Tk()
fenetre.withdraw

label = Label(fenetre, text="V'Sender")
label.pack()




maxchars_uname = 10

def file_path():
    global path
    path = filedialog.askopenfilename()
    print(path)
    avatar.set("{}".format(path))

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

thumbnail = StringVar()
thumbnail.set("Write thumbnail URL here")
thumbnaill = Entry(fenetre, textvariable=thumbnail, width=50)
thumbnaill.pack()

image = StringVar()
image.set("Write image URL here")
imagee = Entry(fenetre, textvariable=image, width=50)
imagee.pack()

author = StringVar()
author.set("Write author name here")
authorr = Entry(fenetre, textvariable=author, width=50)
authorr.pack()

author2 = StringVar()
author2.set("Write author URL here")
authorr2 = Entry(fenetre, textvariable=author2, width=50)
authorr2.pack()

author3 = StringVar()
author3.set("Write author image URL here")
authorr3 = Entry(fenetre, textvariable=author3, width=50)
authorr3.pack()

footer = StringVar()
footer.set("Write footer text here")
footerr = Entry(fenetre, textvariable=footer, width=50)
footerr.pack()

footer2 = StringVar()
footer2.set("Write footer image URL here")
footerr2 = Entry(fenetre, textvariable=footer2, width=50)
footerr2.pack()

field = StringVar()
field.set("Write field here")
fieldd = Entry(fenetre, textvariable=field, width=50)
fieldd.pack()

field2 = StringVar()
field2.set("Write field here")
fieldd2 = Entry(fenetre, textvariable=field2, width=50)
fieldd2.pack()

avatar = tk.StringVar()
avatar.set("Avatar Path")
fieldd2 = tk.Entry(fenetre, textvariable=avatar, width=50)
fieldd2.pack()

booton2 = Button(text ="Choose a avatar file", command=file_path)
booton2.pack()


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


def getThumbnail():
    global thum
    thum=thumbnail.get()


def getImage():
    global imag
    imag=image.get()


def getAuthor():
    global auth
    auth=message.get()


def getAuthor2():
    global auth2
    auth2=message.get()


def getAuthor3():
    global auth3
    auth3=message.get()


def getFooter():
    global foot
    foot=message.get()


def getFooter2():
    global foot2
    foot2=message.get()
    

def getField():
    global fiel
    fiel=message.get()


def getField2():
    global fiel2
    fiel2=message.get()


def getAvatar():
    global avat
    avat=message.get()




def WebhookSender():
    hook = Webhook('{}'.format(ura))

    embed = Embed(
        description='This is the **description** of the embed! :smiley:',
        color=0x5CDBF0,
        timestamp='now'  # sets the timestamp to current time
        )

    image1 = 'https://i.imgur.com/rdm3W9t.png'
    image2 = 'https://i.imgur.com/f1LOr4q.png'

    with open('img.png') as f:
        img = f.read()  # bytes

    hook.modify(name='Bob', avatar=img)


    embed.set_author(name='Author Goes Here', icon_url=image1)
    embed.add_field(name='Test Field', value='Value of the field :open_mouth:')
    embed.add_field(name='Another Field', value='1234 :smile:')
    embed.set_footer(text='Here is my footer text', icon_url=image1)

    embed.set_thumbnail(image1)
    embed.set_image(image2)

    hook.send(embed=embed)


SendBtn = Button(text ="Send !", command=WebhookSender)
SendBtn.pack()

fenetre.mainloop()