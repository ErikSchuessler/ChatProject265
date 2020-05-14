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
    

    def __init__(self, ServerIP, ServerPort, OwnPort, eventHandler):
        self.serverIP=ServerIP
        self.serverPort=12002
        self.ownPort=12001
        self.eventHandler = eventHandler

    def serverFunction(self):
        serverSocket=socket(AF_INET,SOCK_DGRAM)
        serverSocket.bind(('',self.ownPort))
        while True:
            try:
                msg=serverSocket.recvfrom(2048)
                self.do_something(msg[0].decode().strip("'"))
                print("[THEM:] " + msg[0].decode().strip("'"))
                
            except Exception as e:
                print("Server Error:")
                print(e)
                break
       


    def clientFunction(self, msg2Send):
        clientSocket=socket(AF_INET,SOCK_DGRAM)
        #msg=input("[ME:]>")
        clientSocket.connect((self.serverIP, self.serverPort))
        clientSocket.send(msg2Send.encode())
        print("[ME:] "+msg2Send)
        clientSocket.close()

    def run(self):
        serverThread=threading.Thread(target=self.serverFunction)
        serverThread.start()
        
    def do_something(self, message):
           self.eventHandler(message)
