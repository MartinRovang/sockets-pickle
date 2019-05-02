# Import socket module 
import socket                
import pickle

class Client:
    def __init__(self):
        # Define the port on which you want to connect 
        self.port = 5000

    def send(self, info):
        # Create a socket object 
        self.s = socket.socket()
        # connect to the server on local computer 
        self.s.connect(('foxxy.ddns.net', self.port))
        info_byte = pickle.dumps(info)
        self.s.send(info_byte)
        self.s.close()

    def retrieve(self, info):
        # Create a socket object 
        self.s = socket.socket()
        # connect to the server on local computer 
        self.s.connect(('foxxy.ddns.net', self.port))
        info_byte = pickle.dumps(info)
        self.s.send(info_byte)
        retrieved_info = self.s.recv(1024)
        info_retrieve = pickle.loads(retrieved_info)
        # close the connection
        self.s.close()

        return info_retrieve

