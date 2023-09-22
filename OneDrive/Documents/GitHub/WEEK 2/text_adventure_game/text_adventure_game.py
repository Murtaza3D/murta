def introScene():
    print("Hey, sorry to be the bearer of bad news, but you've just died. ")
    print("Welcome to the afterlife baby!")
    print("Our moral judgement systems are down, so you'll have to decide whether you end up in Heaven or Hell")
    directions = ["left", "right"]
    print("So please pick a door")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right")
        userInput = input()
        if userInput == "left":
            hell_lobby()
        elif userInput == "right":
            WelcomeToHeaven()
        else:
            print("Please enter left or right.")

def hell_lobby():
    directions = ["left", "right"]
    print("You open the door on the left. Behind it is a red figure with horns on his head and a pointy tail snaking behind his back.")
    print("'Welcome to hell!' the devil greets you. 'Would you like to see our facilities?'")
    response = ""
    while response not in directions:
        response = input("Where do you look? Options: left/right ")
        if response == "left":
            print("You see blazing, fiery pits.")
            follow_devil()
        elif response == "right":
            print("You see a maggot feeding station the size of petting zoo.")
            follow_devil()
        else: 
            print("Please enter left or right.")

def follow_devil():
    directions = ["forwards", "backwards"]
    print("'Now follow me,' the devil says. He starts to walk forwards.")
    response = ""
    while response not in directions:
        response = input("Where do you go? Options: forwards/backwards ")
        if response == "backwards":
            print("You desperately grab the door behind you only to find it locked.") 
            print("The devil grabs you. 'Leaving so soon?' they ask before throwing you in the fiery pit.")
            print("You spend an eternity trying to get used to the heat.")
            quit()
        elif response == "forwards":
            print("You shuffle behind the devil until both come to the edge of a cliff.")
            print("Now that you're dead, you can enjoy some downtime!', he grins before he pushes you.")
            pitRoom()

def pitRoom():
    directions =["climb","wait"]
    print("You find yourself in a dark pit. What would you like to do?")
    userInput = ""
    while userInput not in ["climb", "wait"]:
        print("Options: climb/wait")
        userInput = input()
        if userInput == "climb":
            print("You try to climb out but slip and fall into a deeper abyss. Your fate is sealed.")
            quit()
        elif userInput == "wait":
            print("You wait in the darkness, and suddenly, a door opens above you. You are lifted out of the pit.")
            WelcomeToHeaven()
        else:
            print("Please enter a valid option")

def WelcomeToHeaven():
    directions=[]
    print("'Welcome to Heaven! You have made it to paradise. Enjoy your eternity of bliss!' says the boy with a halo floating over his head")
    print("Would you like to see our facilities?")
    response = ""
    while response not in directions:
        response = input("Where do you look? Options: left/right ")
        if response == "left":
            print("You see mountains of fluffy dogs and bunnies.")
            follow_angel()
        elif response == "right":
            print("You see rainbows shooting out of a unicorn that's bouncing on a cloud.")
            follow_angel()
        else: 
            print("Please enter left or right.")
def follow_angel():
    directions = [left", "right"]
    print("'Now follow me,' sings the angel. He starts to walk forwards.")
    response = ""
    while response not in directions:
        response = input("Where do you go? Options: forwards/backwards ")
        if response == "backwards":
            print("You desperately grab the door behind you only to find it locked.") 
            print("The devil grabs you. 'Leaving so soon?' they ask before throwing you in the fiery pit.")
            print("You spend an eternity trying to get used to the heat.")
            quit()
        elif response == "forwards":
            print("You shuffle behind the devil until both come to the edge of a cliff.")
            print("Now that you're dead, you can enjoy some downtime!', he grins before he pushes you.")
            pitRoom()

