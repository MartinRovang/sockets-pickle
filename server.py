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
         loaded = self.save_stats(retrieved)
         # send back to client
         loaded_byte = pickle.dumps(loaded)
         c.send(loaded_byte)
         # Close the connection with the client 
         c.close()


   def save_stats(self, player):
      loaded = self.upload_stats(player)
      if loaded == None:
         print('User does not exist, creating %s'%player.name)
         pickle.dump(player, file = open('player_base/%s.pkl'%player.name, 'wb'))
      else:
         return loaded



   def upload_stats(self, player):
      try:
         loaded = pickle.load(file = open('player_base/%s.pkl'%player.name, 'rb'))
         if loaded.password != player.password:
            return 'Password is incorrect'
         else:
            return loaded
      except:
         return 'User %s created'%player.name



         




if __name__ == "__main__":
   server = Server()
   server.start()