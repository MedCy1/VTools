import os
from tkinter import * 
from tkinter import messagebox
import requests
from requests.api import get
from discord_webhooks import DiscordWebhooks

fenetre = Tk()

label = Label(fenetre, text="V'Sender")
label.pack()




maxchars_uname = 10

ura = StringVar()
ura.set("Write Webhook URL here")
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

    
# Webhook URL for your Discord channel.
WEBHOOK_URL = '${link}'

webhook = DiscordWebhooks(WEBHOOK_URL)

webhook.set_content(content='The best cat ever is...', title='Montezuma!', description='Seriously!', \
  url='http://github.com/JamesIves', color=0xF58CBA, timestamp='2018-11-09T04:10:42.039Z')

# Attaches an image
webhook.set_image(url='${imagee}')

# Attaches a thumbnail
webhook.set_thumbnail(url='${thumbnaill}')

# Attaches an author
webhook.set_author(name='${authorr}', url='${authorr2}', icon_url='${authorr3}')

# Attaches a footer
webhook.set_footer(text='${footerr}', icon_url='${footerr2}')

# Appends a field
webhook.add_field(name='${fieldd}', value='${fieldd2}')

booton = Button(text ="Send !", command=webhook.send)

booton.pack()


fenetre.mainloop()
