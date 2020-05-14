import tkinter as tk
from socket import *
from Talk import Talk
import threading
import sys

windowHeight0 = 700
windowWidth0 = 300
windowHeight = 500
windowWidth = 500

name = "ME"
ServerIP = "localhost"
OwnPort = 12002
ServerPort = 12001


def on_notify(message):
    receive(message)

def endStartup():
    global root0   
    root0.destroy()

def setName(nameToSet):
    global name
    name = nameToSet

def setOwnPort(ownPortToSet):
    global OwnPort
    OwnPort = ownPortToSet

def setServerPort(serverPortToSet):
    global ServerPort
    ServerPort = serverPortToSet


root0 = tk.Tk()

canvas0 = tk.Canvas(root0, height=windowHeight0, width=windowWidth0)
canvas0.pack()

frame0 = tk.Frame(root0, bg='#d6d6d6')
frame0.place(relwidth=1, relheight=1)

label = tk.Label(frame0, text="Welcome to IM Chat 2020")
label.pack(anchor='center')

##Name Entry

nameQLabel = tk.Label(frame0, text="What is your name?")
nameQLabel.place(relwidth = 0.85, relheight = 0.1, relx=0.075, rely=0.1)

nameEntry = tk.Entry(frame0)
nameEntry.place(relwidth=0.775, relheigh=0.03, relx=0.075, rely=0.2)

nameEnterButton = tk.Button(root0, text="Enter", command= lambda: setName(nameEntry.get()))
nameEnterButton.place(relwidth=0.225, relheigh=0.03, relx=0.7, rely=0.2)

##Own Port Entry

ownPortQLabel = tk.Label(frame0, text="What is YOUR port number?")
ownPortQLabel.place(relwidth = 0.85, relheight = 0.1, relx=0.075, rely=0.25)

ownPortEntry = tk.Entry(frame0)
ownPortEntry.place(relwidth=0.775, relheigh=0.03, relx=0.075, rely=0.35)

ownPortEnterButton = tk.Button(root0, text = "Enter", command= lambda: setOwnPort(ownPortEntry.get()))
ownPortEnterButton.place(relwidth=0.225, relheigh=0.03, relx=0.7, rely=0.35)

##ServerPortEntry

serverPortQLabel = tk.Label(frame0, text="What is THEIR port number?")
serverPortQLabel.place(relwidth = 0.85, relheight = 0.1, relx=0.075, rely=0.40)

serverPortEntry = tk.Entry(frame0)
serverPortEntry.place(relwidth=0.775, relheigh=0.03, relx=0.075, rely=0.5)

serverPortEnterButton = tk.Button(root0, text = "Enter", command= lambda: setServerPort(serverPortEntry.get()))
serverPortEnterButton.place(relwidth=0.225, relheigh=0.03, relx=0.7, rely=0.5)

##Begin chat

EnterButton = tk.Button(root0, text = "Begin chatting!", command= endStartup)
EnterButton.place(relwidth=0.85, relheigh=0.2, relx=0.075, rely=0.6)


root0.mainloop()

root = tk.Tk()



def receive(message):
    newMessage = messageBox.cget("text") + '\n' + message
    messageBox.config(text= newMessage, anchor='nw')


def send(name, textEntry):
    newMessageToPrint = messageBox.cget("text") + '\n' + "[" + name + ":] " + textEntry
    newMessageToSend = "["+name+":] "+ textEntry
    messageBox.config(text=newMessageToPrint, anchor='nw')
    talk1.clientFunction(newMessageToSend)
   

def endChat():
    global root
    root.destroy()

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

sendButton = tk.Button(root, text="Send", command= lambda: send(name, textEntry.get()))
sendButton.place(relwidth=0.2,relheigh=0.1, relx=0.725, rely=0.83)

talk1 = Talk(ServerIP,ServerPort,OwnPort, on_notify)



talk1.run()

#register event handler for the event you are raising in Talk
#messageBox.bind('SendText', textEntry.get())


root.mainloop()
