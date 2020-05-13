from socket import *
import threading
import sys


CURSOR_UP_ONE = '\x1b[1A' # move the cursor to previous line on the screen
ERASE_LINE = '\x1b[2K'    # erase the content of the line on the screen

class Talk:

    '''
    AS a client: you have to know server's IP and Port number
    AS a server: you need to know the port number that
                 you use to provide services
    '''
    

    def __init__(self, ServerIP, ServerPort, OwnPort):
        self.serverIP=ServerIP
        self.serverPort=12001
        self.ownPort=12002

    def serverFunction(self):
        serverSocket=socket(AF_INET,SOCK_DGRAM)
        serverSocket.bind(('',self.ownPort))
        #serverSocket.listen(1)
        #connectionSocket,add=serverSocket.accept()

        #print(str(add[0])+","+str(add[1])+" connects")
        while True:
            try:
                msg=serverSocket.recvfrom(2048)
                print("")
                print("[THEM:] " + msg[0].decode().strip("'"))
                print("")
                print("[PRESS 'Enter' TO BEGIN TYPING...]")

                # Do not need to close connection as UDP is connectionless protocol

                # if msg.upper()=="QUIT":
                    # connectionSocket.close()
                    # break
            except Exception as e:
                print("Server Error:")
                print(e)
                break
        #connectionSocket.close()

    def clientFunction(self):
        clientSocket=socket(AF_INET,SOCK_DGRAM)
        msg=input("[ME:]>")
        clientSocket.connect((self.serverIP, self.serverPort))
        clientSocket.send(msg.encode())

        #test change

        #raise event here
        do_something()

        while True:
            try:
                msg=input("[ME:]>")
                # print("[ME:]> "+msg) 
                # print out the user input on the screen and overwrites the previous line
                # print(CURSOR_UP_ONE+ERASE_LINE+"[ME:]> "+msg) 
                clientSocket.send(msg.encode())

                #raise event here

                if msg.upper()=="QUIT":
                    clientSocket.close()
                    break
            except Exception as e:
                print("Client Error:")
                print(e)
                break
        clientSocket.close()

    def run(self):
        serverThread=threading.Thread(target=self.serverFunction)
        clientThread=threading.Thread(target=self.clientFunction)
        serverThread.start()
        clientThread.start()

    
    def do_something(self, update):
           # do whatever I need to do
           print("I've changed\n")
           update()