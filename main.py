from client import Client
from player import Player
import time
from easygui import *

# player1 = Player('peder')
# player1.health = 10


class Game:
    def __init__(self):
        # Initiate client
        self.client = Client()
        
        # User registrer
        msg = "Register new player/login"
        title = "Demo of multpasswordbox"
        fieldNames = ["User ID", "Password"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = multpasswordbox(msg, title, fieldNames)

        # make sure that none of the fields was left blank
        while 1:
            if fieldValues == None: 
                break
            errmsg = ""
            for i in range(len(fieldNames)):
                if fieldValues[i].strip() == "":
                    errmsg = errmsg + ('"%s" is a required field.\n\n' %fieldNames[i])
            if errmsg == "": 
                break # no problems found
            fieldValues = multpasswordbox(errmsg, title, fieldNames, fieldValues)

        player_name, password = fieldValues
        new_player = Player(player_name, password)
        loaded = self.client.retrieve(new_player)
        if type(loaded) == str:
            print(loaded)
        else:
            print('health: %s'%loaded.health)


if __name__ == "__main__":
    game = Game()