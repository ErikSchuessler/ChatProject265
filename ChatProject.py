import tkinter as tk
from socket import *
from Talk import Talk
import threading
import sys

windowHeight0 = 300
windowWidth0 = 300
windowHeight = 500
windowWidth = 500
endButtonXPos = 100
sendButtonXPos = 400

ServerIP = "localhost"
ServerPort = 12001
OwnPort = 12002


def on_notify():
      print("OK, I'm up-to-date")


#root0 = tk.Tk()

#canvas0 = tk.Canvas(root0, height=windowHeight0, width=windowWidth0)
#canvas0.pack()

#frame0 = tk.Frame(root0, bg='#d6d6d6')
#frame0.place(relwidth=1, relheight=1)

#label = tk.Label(frame0, text="Welcome to IM Chat 2020")
#label.pack(anchor='center')

#label = tk.Label(frame0, text="Who would you like to chat with?")
#label.pack(anchor='center', side='bottom')

#nameEntry = tk.Entry(frame0)
#nameEntry.place(relwidth=0.85, relheigh=0.1, relx=0.075, rely=0.7)


#root0.mainloop()

root = tk.Tk()


def send(textEntry):
    messageBox.config(text="[ME:] "+ textEntry, anchor='nw')
    print("You sent:", textEntry)

def endChat():
    global root
    root.quit()
    print("Chat ended.")

# put event handler here - just a method that handles events


canvas = tk.Canvas(root, height=windowHeight, width=windowWidth)
canvas.pack()

frame = tk.Frame(root, bg='#d6d6d6')
frame.place(relwidth=1, relheight=1)

label = tk.Label(frame, text="IM Chat 2020 by Erik, Lily, Danny")
label.place(relwidth = 0.5, relheight = 0.05, relx=0.25, rely=0.1)

messageBox = tk.Message(frame, bg='white', width = 425)
messageBox.place(relwidth = 0.85, relheight = 0.5, relx=0.075, rely=0.175)

textEntry = tk.Entry(frame, text='Enter text...')
textEntry.place(relwidth=0.85, relheigh=0.1, relx=0.075, rely=0.7)

endChatButton = tk.Button(root, text="End Chat", command=endChat)
endChatButton.place(relwidth=0.2,relheigh=0.1, relx=0.075, rely=0.83)

sendButton = tk.Button(root, text="Send", command= lambda: send(textEntry.get()))
sendButton.place(relwidth=0.2,relheigh=0.1, relx=0.725, rely=0.83)

talk1 = Talk(ServerIP,ServerPort,OwnPort)

talk1.do_something(on_notify)
talk1.run()

#register event handler for the event you are raising in Talk
#messageBox.bind('SendText', textEntry.get())


root.mainloop()

