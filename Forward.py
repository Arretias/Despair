#Despair -  A text based adventure game.


#The Player Class, initialized upon starting a new game.
class Player:
    def __init__(self, name):
        self.name = name
        self.hit_points = 100
        self.inventory = []

        self.currentroom = 5


#Rooms 1-9 Ordered in a list, along with room info stored in lists for each room.
rooms = {1:["NW", "Locked"],
         2:["N", "Locked"],
         3:["NE", "Locked"],
         4:["W", "Locked"],
         5:["C", "Unlocked"],
         6:["E", "Locked"],
         7:["SW", "Locked"],
         8:["S", "Unlocked"],
         9:["SE", "Locked"]}


def Intro():
    #Main - Intro and Player Initialization.
    print("----- Despair -----")
    print("Welcome to Despair. Please enter your name below to begin the game.")

    while True:
        playername = input("")
        if playername.isalpha():
            player = Player(playername.title())
            break
        else:
            print("Invalid Name - Please use only alphabetical characters.")

    print("Welcome " + player.name + ", your adventure is about to begin.")


def Main_Menu():
    print("This is where the main menu will be")

#Game code, running from functions and classes pre-defined.
Intro()
