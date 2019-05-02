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
        msg = "Register new player"
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
                    errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
            if errmsg == "": 
                break # no problems found
            fieldValues = multpasswordbox(errmsg, title, fieldNames, fieldValues)

        print("Reply was:", fieldValues)

        player_name = fieldValues[0]
        login = self.client.retrieve(player_name)
        if login == None:
            new_player = Player(player_name)
            self.client.send(new_player)

if __name__ == "__main__":
    game = Game()