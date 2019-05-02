import socket                
import pickle
from player import Player


class Server:

   def __init__(self):
      # Socket object
      self.s = socket.socket()          
      print ("Socket successfully created")
      
      # Reserve port
      self.port = 5000
      
      # bind port
      self.s.bind(('0.0.0.0', self.port))     
      print("socket binded to %s" %(self.port) )

      # Set to listen
      self.s.listen(5)
      print ("socket is listening"  )          
   

   def start(self):
      # a forever loop until we interrupt it or  
      # an error occurs 
      while True: 
         # Establish connection with client. 
         c, addr = self.s.accept()
         print('Got connection from', addr )
         # Retrieved from client
         retrieved = pickle.loads(c.recv(1024))
         print(retrieved)
         if type(retrieved) != str:
            self.save_stats(retrieved)
            # send back to client
            # c.send(b'Info saved')
            # Close the connection with the client 
            c.close()
         else:
            loaded = self.upload_stats(retrieved)
            loaded_byte = pickle.dumps(loaded)
            c.send(loaded_byte)
            c.close()

      
   def save_stats(self, player):
      pickle.dump(player, file = open('player_base/%s.pkl'%player.name, 'wb'))

   
   def upload_stats(self, player_name):
      try:
         loaded = pickle.load(file = open('player_base/%s.pkl'%player_name, 'rb'))
      except:
         print('User does not exist')
         return None
      return loaded



         




if __name__ == "__main__":
   server = Server()
   server.start()