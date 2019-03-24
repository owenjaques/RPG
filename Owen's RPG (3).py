#a pretty basic console based text game. I updated it to python 3 in 2018 as well as added some features making it easier to play. May play around with it some more

inventory = ["compass"]
stuff_that_happened = []

north = ("go north", "north", "n")
south = ("go south","south", "s")
west = ("go west", "west", "w")
east = ("go east", "east", "e")

ways_to_say_inventory = ("inventory", "i")

def basic_instructions():
    print("Would you like the basic instructions?")
    feedback = input(">").lower()
    if feedback == "yes":
        print("To go places use go (direction). To take things use take (item). To kill things use kill (creature) with (item). To see your inventory use inventory.")
        detailed_instructions()
    elif feedback == "no":
        start()
    else:
        print("Please type yes or no.")
        basic_instructions()

def detailed_instructions():
    print("Would you like the detailed instructions?")
    feedback = input(">").lower()
    if feedback == "yes":
        print("To eat use eat (food). To give things to creatures use give (creature) (item). To sleep use sleep in bed. To put something in something else use put (item) in (item). To quickly end the game use kill myself. The directions you may go are north, south, east, west, up, down and sometimes back.")
        start()
    elif feedback == "no":
        start()
    else:
        print("Please type yes or no.")
        detailed_instructions()

def start():
    print("Are you ready to start?")
    feedback = input(">").lower()
    if feedback == "yes":
        intro()
    elif feedback == "no":
        starter()
    else:
        print("Please type yes or no.")
        start()

def starter():
    print("Sure you're not ready to start?")
    feedback = input(">").lower()
    if feedback == "yes":
        print("Too bad.")
        intro()
    elif feedback == "no":
        print("Let's start then.")
        intro()
    else:
        intro()

def intro():
    print("You find yourself alone in a dungeon. All you have is your trusty compass and good spirits. You see a flickering light coming from the south. What do you do?")
    feedback = input(">").lower()
    if feedback in south:
        small_room()
    elif feedback == "cheat":
        inventory.append("sword")
        inventory.append("cheese")
        inventory.append("key")
        inventory.append("candle")
        inventory.append("knife")
        inventory.append("gas mask")
        inventory.append("ruby")
        stuff_that_happened.append("sword")
        stuff_that_happened.append("cheese")
        stuff_that_happened.append("key")
        stuff_that_happened.append("candle")
        stuff_that_happened.append("knife")
        stuff_that_happened.append("gas mask")
        stuff_that_happened.append("ruby")
        stuff_that_happened.append("hobgoblin")
        print(inventory)
        intro()
    elif feedback == "kill myself":
        print("You die.")
    elif feedback in ways_to_say_inventory:
        print(inventory)
        intro()
    elif feedback in north or west or east:
        print("You can't go that way.")
        intro()
    else:
        print("What language are you speaking?")
        intro()

def first_room():
    print("You're back where you started.")
    feedback = input(">").lower()
    if feedback in south:
        small_room()
    elif feedback == "kill myself":
        print("You die.")
    elif feedback in ways_to_say_inventory:
        print(inventory)
        first_room()
    elif feedback in north or west or east:
        print("You can't go that way.")
        first_room()
    else:
        print("What language are you speaking?")
        first_room()

def small_room():
    if "candle" in stuff_that_happened:
        print("You are in a small room. There is a small wooden table. There are stairs with a door at the top to the east and a passageway to the west.")
    else:
        print("You are in a small room. There is a small wooden table, sitting atop that table is a candle dimly illuminating the room. There are stairs with a door at the top to the east and a passageway to the west.")
    feedback = input(">").lower()
    if feedback in east:
            if "key" in inventory:
                print("The door creaks open.")
                kitchen()
            else:
                print("The door is locked.")
                small_room()
    elif feedback == "kill myself":
        print("You die.")
    elif feedback in north:
        first_room()
    elif feedback in ways_to_say_inventory:
        print(inventory)
        small_room()
    elif feedback == "take candle":
        print("Taken")
        inventory.append("candle")
        stuff_that_happened.append("candle")
        small_room()
    elif feedback in west:
        print("You travel down the passageway.")
        larger_room()
    elif feedback in south:
        print("You can't go that way.")
        small_room()
    else:
        print("What language are you speaking?")
        small_room()

def larger_room():
    if "candle" in inventory:
        print("You are in a larger room with a tall curving roof. There is the passageway to the east and another room to the south.")
    else:
        print("It's really dark, you may trip, hit your head and die.")
    feedback = input(">").lower()
    if feedback in east:
        print("You travel down the passageway.")
        small_room()
    elif feedback == "kill myself":
        print("You die.")
    elif feedback in ways_to_say_inventory:
        print(inventory)
        larger_room()
    elif feedback in south:
            if "candle" in inventory:
                large_room()
            else:
                print("You stumble into the the next room only to step on a bear trap you couldn't see. You die slowly and painfully.")
    elif feedback in west or north:
        print("You can't go that way.")
        larger_room()
    else:
        print("What language are you speaking?")
        larger_room()

def large_room():
    print("You are in a large room with a strange statue of a pear in the centre. There is a crawlway to the east and the other room to the north.")
    feedback = input(">").lower()
    if feedback in north:
        larger_room()
    elif feedback == "kill myself":
        print("You die.")
    elif feedback in ways_to_say_inventory:
        print(inventory)
        large_room()
    elif feedback in east:
        key_room()
    elif feedback in west or south:
        print("You can't go that way.")
        large_room()
    else:
        print("What language are you speaking?")
        large_room()        

def key_room():
    if "key" in stuff_that_happened:
        print("You immediately see several empty beer bottles strewn across the floor. Next you see a giant man lying on the floor, barf covering his chest and face. He is clearly asleep. The only exit is the crawlway that you came in through.")
    else:
        print("You immediately see several empty beer bottles strewn across the floor. Next you see a giant man lying on the floor, barf covering his chest and face. You see a key tied to his belt. He is clearly asleep. The only exit is the crawlway that you came in through.")
    feedback = input(">").lower()
    if feedback in west:
        large_room()
    elif feedback == "kill myself":
        print("You die.")
    elif feedback in ways_to_say_inventory:
        print(inventory)
        key_room()
    elif feedback == "take key":
        print("Taken")
        inventory.append("key")
        stuff_that_happened.append("key")
        key_room()
    elif feedback in ways_to_say_inventory:
        print(inventory)
        key_room()
    elif feedback == "go back":
        large_room()
    elif feedback in east or north or south:
        print("You can't go that way.")
        key_room()
    else:
        print("What language are you speaking?")
        key_room()

def kitchen():
    if "knife" in stuff_that_happened:
        print("You are in a large commercial kitchen. You can see a dining room to the south and a small pantry appears to be to the east.")
    else:
        print("You open the door to find yourself in a large commercial kitchen. Strangely there is only one knife sitting atop the counter. You can see a dining room to the south and a small pantry appears to be to the east.")
    feedback = input(">").lower()
    if feedback == "take knife":
        print("Taken")
        inventory.append("knife")
        stuff_that_happened.append("knife")
        kitchen()
    elif feedback == "kill myself":
        print("You die.")
    elif feedback in ways_to_say_inventory:
        print(inventory)
        kitchen()
    elif feedback in west:
        small_room()
    elif feedback in east:
        pantry()
    elif feedback in south:
        dining_room()
    elif feedback in north:
        print("You can't go that way.")
        kitchen()
    else:
        print("What language are you speaking?")
        kitchen()

def pantry():
    if "cheese" in stuff_that_happened:
        print("You are in a small pantry smelling vaguely of cheese.")
    else:
        print("You are in small pantry smelling vaguely of cheese. There is only a small piece of cheese left.")
    feedback = input(">").lower()
    if feedback in west:
        kitchen()
    elif feedback == "kill myself":
        print("You die.")
    elif feedback in ways_to_say_inventory:
        print(inventory)
        pantry()
    elif feedback == "take cheese":
        print("Taken")
        inventory.append("cheese")
        stuff_that_happened.append("cheese")
        pantry()
    elif feedback == "go back":
        kitchen()
    elif feedback == "eat cheese":
        print("You attempt to eat the cheese but are thrown of by it's terrible smell.")
        pantry()
    elif feedback in north or east or south:
        print("You can't go that way.")
        pantry()
    else:
        print("What language are you speaking?")
        pantry()

def dining_room():
    print("You are in what once was a spacious and luxurious dining room. The table is covered in mouldy rotten food and spiders hang from the ceiling, their webs cover everything. The webs are all covered in a layer of dust. It seems asthough no one has been here for years. There is a ballroom to the south.")
    feedback = input(">").lower()
    if feedback == "eat food":
        print("You take one bite of the food and immediately barf out your innards, killing you just after you see your lungs fly out of your mouth and on to the table.")
    elif feedback == "kill myself":
        print("You die.")
    elif feedback in ways_to_say_inventory:
        print(inventory)
        dining_room()
    elif feedback in north:
        kitchen()
    elif feedback in south:
        ballroom()
    elif feedback in west or east:
        print("You can't go that way.")
        dining_room()
    else:
        print("What language are you speaking?")
        dining_room()

def ballroom():
    if "troll" in stuff_that_happened:
        print("You are in a majestic ballroom. There are french doors to the west and a stairway to the east.")
    else:
        print("You are in a majestic ballroom. There are french doors to the west and a massive troll smelling strongly of cheese to the east. He appears to be guarding a stairway up.")
    feedback = input(">").lower()
    if feedback in west:
        courtyard()
    elif feedback == "kill myself":
        print("You die.")
    elif feedback in ways_to_say_inventory:
        print(inventory)
        ballroom()
    elif feedback in north:
        dining_room()
    elif feedback == "kill troll with knife":
            if "knife" in inventory:
                print("You stab the troll in his stomach. He laughs at your puny attempt to kill him and eats your head.")
            else:
                print("You don't have the knife.")
                ballroom()
    elif feedback == "give troll cheese":
            if "cheese" in inventory:
                print("The troll laughs merrily and takes the cheese and allows you to pass.")
                inventory.remove("cheese")
                stuff_that_happened.append("troll")
                hall()
            else:
                print("You don't have the cheese.")
                ballroom()
    elif feedback in east:
            if "troll" in stuff_that_happened:
                hall()
            else:
                print("The troll eats your head.")
    elif feedback == "go up":
        hall()
    elif feedback in south:
        print("You can't go that way.")
        ballroom()
    else:
        print("What language are you speaking?")
        ballroom()

def courtyard():
    print("You are in a old courtyard surrounded by forest and the house.")
    feedback = input(">").lower()
    if feedback in east:
        ballroom()
    elif feedback == "kill myself":
        print("You die.")
    elif feedback in ways_to_say_inventory:
        print(inventory)
        courtyard()
    elif feedback in north:
        north_forest()
    elif feedback in west:
        west_forest()
    elif feedback in south:
        south_forest()
    else:
        print("What language are you speaking?")
        courtyard()

def hall():
    print("You are in a hall with the stairs to the east and bedrooms to the north and west. Through a window you can see what appears to be an endless forest.")
    feedback = input(">").lower()
    if feedback in east:
        ballroom()
    elif feedback == "kill myself":
        print("You die.")
    elif feedback in ways_to_say_inventory:
        print(inventory)
        hall()
    elif feedback == "go down":
        ballroom()
    elif feedback in north:
        northbedroom()
    elif feedback in west:
        westbedroom()
    elif feedback in south:
        print("You can't go that way.")
        hall()
    else:
        print("What language are you speaking?")
        hall()

def northbedroom():
    if "sword" in stuff_that_happened:
        print("You are in the master bedroom. There is a disgusting looking bed in the centre of it. There is a bathroom to the west.")
    else:
        print("You are in the master bedroom. There is a disgusting looking bed in the centre of it. There is a bathroom to the west. There is a sword hanging on the wall above the bed.")
    feedback = input(">").lower()
    if feedback == "sleep in bed":
        print("You fall asleep but never wake up.")
    elif feedback == "kill myself":
        print("You die.")
    elif feedback == "take sword":
        print("Taken")
        inventory.append("sword")
        stuff_that_happened.append("sword")
        northbedroom()
    elif feedback in ways_to_say_inventory:
        print(inventory)
        northbedroom()
    elif feedback in west:
        bathroom()
    elif feedback in south:
        hall()
    elif feedback in north or east:
        print("You can't go that way.")
        northbedroom()
    else:
        print("What language are you speaking?")
        northbedroom()        
        
def westbedroom():
    print("You are in the west bedroom. There is a disgusting looking bed in the left of it. There is a bathroom to the north.")
    feedback = input(">").lower()
    if feedback == "sleep in bed":
        print("You fall asleep but never wake up.")
    elif feedback == "kill myself":
        print("You die.")
    elif feedback in ways_to_say_inventory:
        print(inventory)
        westbedroom()
    elif feedback in north:
        bathroom()
    elif feedback in east:
        hall()
    elif feedback in west or south:
        print("You can't go that way.")
        westbedroom()
    else:
        print("What language are you speaking?")
        westbedroom()

def bathroom():
    if "ruby" in stuff_that_happened:
        print("You are in a disgusting bathroom. Thankfully you cannot smell it thanks to the mask.")
    elif "gas mask" in stuff_that_happened:
        print("You are in a disgusting bathroom. Thankfully you cannot smell it thanks to the mask. There is a ruby in the sink.")
    else:
        print("You are in a disgusting bathroom. The smell is enough to kill a horse. There is a ruby in the sink.")
    feedback = input(">").lower()
    if feedback in south:
        westbedroom()
    elif feedback == "kill myself":
        print("You die.")
    elif feedback in east:
        northbedroom()
    elif feedback in ways_to_say_inventory:
        if "gas mask" in stuff_that_happened:
            print(inventory)
            bathroom()
        else:
            print("You did'nt get out quick enough the smell destroys your nostrils and you turn into a pile of acid.")
    elif feedback == "take ruby":
        if "gas mask" in stuff_that_happened:
            print("Taken")
            inventory.append("ruby")
            stuff_that_happened.append("ruby")
            bathroom()
        else:
            print("You did'nt get out quick enough the smell destroys your nostrils and you turn into a pile of acid.")
    else:
        if "gas mask" in stuff_that_happened:
            print("What language are you speaking?")
            bathroom()
        else:
            print("You did'nt get out quick enough the smell destroys your nostrils and you turn into a pile of acid.")

def north_forest():
    print("You are in a forest.")
    feedback = input(">").lower()
    if feedback in south:
        courtyard()
    elif feedback == "kill myself":
        print("You die.")
    elif feedback in west:
        west_forest()
    elif feedback in north:
        north_forest()
    elif feedback in east:
        north_forest()
    elif feedback in ways_to_say_inventory:
        print(inventory)
        north_forest()
    else:
        print("What language are you speaking?")
        north_forest()

def south_forest():
    print("You are in a forest.")
    feedback = input(">").lower()
    if feedback in north:
        courtyard()
    elif feedback == "kill myself":
        print("You die.")
    elif feedback in west:
        west_forest()
    elif feedback in south:
        clearing()
    elif feedback in east:
        south_forest()
    elif feedback in ways_to_say_inventory:
        print(inventory)
        south_forest()
    else:
        print("What language are you speaking?")
        south_forest()

def west_forest():
    print("You are in a forest.")
    feedback = input(">").lower()
    if feedback in east:
        courtyard()
    elif feedback == "kill myself":
        print("You die.")
    elif feedback in west:
        west_forest()
    elif feedback in north:
        north_forest()
    elif feedback in south:
        south_forest()
    elif feedback in ways_to_say_inventory:
        print(inventory)
        west_forest()
    else:
        print("What language are you speaking?")
        west_forest()

def clearing():
    if "sword in stone" in stuff_that_happened:
        print("You are in a clearing. You feel the magic in the air. There is a passageway going down.")
    else:
        print("You come into a clearing. You can feel magic in the air; there is a stone with a hole in it in the centre with this engraving 'Utpay ouryay ordsway intoway ethay onestay'")
    feedback = input(">").lower()
    if feedback in north:
        south_forest()
    elif feedback == "kill myself":
        print("You die.")
    elif feedback in south:
        west_forest()
    elif feedback in east:
        south_forest()
    elif feedback in west:
        west_forest()
    elif feedback in ways_to_say_inventory:
        print(inventory)
        clearing()
    elif feedback == "go down":
            if "sword in stone" in stuff_that_happened:
                shrine()
            else:
                print("You can't go that way.")
    elif feedback == "put sword in stone":
            if "sword" in inventory:
                print("You put your sword in the stone. The stone starts sinking into the ground revealing a passageway going down.")
                stuff_that_happened.append("sword in stone")
                inventory.remove("sword")
                clearing()
            else:
                print("You don't have the sword.")
                clearing()
    else:
        print("What language are you speaking?")
        clearing()

def shrine():
    if "gas mask" in stuff_that_happened:
        print("You are in a shrine. The dead body of the hobgoblin is lying in a pool of green blood. Only now do you realize there is a gem shaped hole in an altar in the centre.")
    elif "hobgoblin" in stuff_that_happened:
        print("You are in a shrine. The dead body of the hobgoblin wearing his gas mask is lying in a pool of green blood. Only now do you realize there is a gem shaped hole in an altar in the centre.")
    else:
        print("You are in a shrine. But suddenly a hobgoblin wearing a gas mask jumps out from behind a vase and says 'This is my gold lassie'.")
    feedback = input(">").lower()
    if feedback == "go up":
        clearing()
    elif feedback == "kill hobgoblin with knife":
        if "knife" in inventory:
            print("The knife goes deep into his spleen killing him instantly. Finally something goes your way.")
            stuff_that_happened.append("hobgoblin")
            shrine()
        else:
            print("You don't have the knife.")
            shrine()
    elif feedback == "kill myself":
        print("You die.")
    elif feedback in ways_to_say_inventory:
        print(inventory)
        shrine()
    elif feedback == "take gas mask":
        if "hobgoblin" in stuff_that_happened:
            print("Taken")
            inventory.append("gas mask")
            stuff_that_happened.append("gas mask")
            shrine()
        else:
            print("He's still wearing it.")
            shrine()
    elif feedback == "put ruby in altar":
        if "ruby" in inventory:
            print("You place the ruby into the altar and colour falls from the ceiling. You see colours you didn't know existed erupt from the walls. Suddenly everything goes black. When light returns the world is white.")
            print("THE END")
            credits()
        else:
            print("You don't have the ruby.")
            shrine()
    elif feedback == "take gold":
        if "hobgoblin" in stuff_that_happened:
            print("It's too heavy for a single man to carry.")
            shrine()
        else:
            print("The hobgoblin enraged, kills you.")
    elif feedback in west or south or north or east:
        print("You can't go that way.")
        shrine()
    else:
        print("What language are you speaking?")
        shrine()  

def credits():
    feedback = input("Would you like the credits?").lower()
    if feedback == "yes":
        print("Made by Owen Jaques")
        print("Finished Wednesday December 23rd 2015, edited Sunday September 30th 2018")
        print("Originally written in Python 2.7.1, changed to python 3.7")
    elif feedback == "no":
        print("Too bad this was hard to make.")
        print("Made by Owen Jaques")
        print("Finished Wednesday December 23rd 2015, edited Sunday September 30th 2018")
        print("Originally written in Python 2.7.1, changed to python 3.7")
    else:
        print("I didn't get that but you can see them anyways.")
        print("Made by Owen Jaques")
        print("Finished Wednesday December 23rd 2015, edited Sunday September 30th 2018")
        print("Originally written in Python 2.7.1, changed to python 3.7")

basic_instructions()