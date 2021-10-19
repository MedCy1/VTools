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
field.set("Write field Name")
fieldd = Entry(fenetre, textvariable=field, width=50)
fieldd.pack()

field2 = StringVar()
field2.set("Write field Text here")
fieldd2 = Entry(fenetre, textvariable=field2, width=50)
fieldd2.pack()

avatar = tk.StringVar()
avatar.set("Avatar Path")
fieldd2 = tk.Entry(fenetre, textvariable=avatar, width=50)
fieldd2.pack()

description = tk.StringVar()
description.set("Write description here")
descriptionn= tk.Entry(fenetre, textvariable=description, width=50)
descriptionn.pack()

nameWebhook = tk.StringVar()
nameWebhook.set("Write Webhook name here")
nameWebhookk= tk.Entry(fenetre, textvariable=nameWebhook, width=50)
nameWebhookk.pack()

booton2 = Button(text ="Choose a avatar file", command=file_path)
booton2.pack()




link=ura.get()
#https://discord.com/api/webhooks/898286370693472296/nujOOXcKGvMwFa7VR2-GU8IF84oye2DwXe3f83J9G7W2LZ5TDKHTfqcaxdFpHnRYqbUB

uname=username.get()

thum=thumbnail.get()

imag=image.get()

auth=author.get()

auth2=author2.get()

auth3=author3.get()

foot=footer.get()

foot2=footer2.get()

fiel=field.get()

fiel2=field2.get()

avat=avatar.get()

desc=description.get()

Wname=nameWebhook.get()




def WebhookSender():
    hook = Webhook('{}'.format(link))

    embed = Embed(
        description='{}'.format(desc),
        color=0x5CDBF0,
        timestamp='now'
        )

    hook.modify(name='{}'.format(Wname), avatar=avat)


    embed.set_author(name='{}'.format(auth), icon_url=auth3)
    embed.add_field(name='{}'.format(fiel), value='{}'.format(fiel2))
    embed.set_footer(text='{}'.format(foot), icon_url=foot2)

    embed.set_thumbnail(thum)
    embed.set_image(imag)

    hook.send(embed=embed)


SendBtn = Button(text ="Send !", command=WebhookSender)
SendBtn.pack()

fenetre.mainloop()