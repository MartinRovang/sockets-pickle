from client import Client
from player import Player
import time


# player1 = Player('peder')
# player1.health = 10


client = Client()
# client.send(player1)

info = client.retrieve('peder')

print(info.health)

time.sleep(5.5)  
