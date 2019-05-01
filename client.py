# Import socket module 
import socket                
import pickle

class Client:
    def __init__(self):
        # Create a socket object 
        self.s = socket.socket()         

        # Define the port on which you want to connect 
        self.port = 5000

    def send(self, info):
        # connect to the server on local computer 
        self.s.connect(('192.168.0.158', self.port))
        info_byte = pickle.dumps(info)
        self.s.send(info_byte)
        self.s.close()


    def retrieve(self, string):
        # connect to the server on local computer 
        self.s.connect(('192.168.0.158', self.port))
        string_byte = pickle.dumps(string)
        self.s.send(string_byte)
        retrieved_info = self.s.recv(1024)
        info_retrieve = pickle.loads(retrieved_info)
        # close the connection
        self.s.close()

        return info_retrieve

