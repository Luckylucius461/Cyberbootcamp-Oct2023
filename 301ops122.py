import random
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 
# Introduction
name = input("What is your name, adventurer?\n")
print("Greetings, " + name + ". Let us go on a quest!")
print("You find yourself by the entrance of a dungeon.")
print("will you survive?\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the dungeon?\nyes/no\n")
    if response == "yes":
        print("You head into the dungeon. You can feel the dampness of the walls and floor as you try and peer through the darkness.\n")
    elif response == "no":
        print("Your family will starve because of your cowardess, feel ashamed adventurer " + name + ".")
        quit()
    else:
        print("error not an option.\n")
# Next part of game
response = ""
while True:
    print("You walk down the damp halls of the dungeon, finally after what feels like ages of walking you come to the first intersection")
    print("To your left, you see a faint light flickering.")
    print("To your right, there is what looks to be a descarded libary.")
    print("There is a rock wall infront of you.")
    print("Behind you is the dungeons exit.\n")
    response = input("What direction do you move?\nleft/right/backward\n")
    if response == "left":
        print("You turn and walk down the hallway but notice an old arrow trap")
        fight = input("try and disarm the trap? y/n\n")
        if  fight == "y":
            print("10 sided dice rolled to see if you are skilled enough to disarm the trap, you need a 5 or higher")
            number = random.randint(1, 10)
            if number >= 5:
                print(f"you have disarmed the trap with a roll of {number} and found a pile of gold. You excape the dungeon a rich man.")
                response = ""
            else: print("You rolled less than 5 you explode along with the arrow trap.")
            quit()
        else: print("you try and out run the arrows, you cannot.")
       
    elif response == "right":
        print("You walk into the libary examining all the torn books and destroyed bookshelves.\n")
        glistin = input("you notice two sets of stairs in the libary. one on the left going down and one on the right going up. which do you pick?\n")
        if glistin == "left":
            print("You walk downstairs and immediately an unplesent stench of the undead assaults you, as you reach the bottom floor you see an Undead lich guarding a pile of old Relics.")
            print(" you panic and look around for a moment. you notice a bow laying just next to the stairs and grab it")
            lich = input("\nDo you shoot the Lich or try to run.  shoot/run\n")
            if lich == "shoot":
                arrow = random.randint(1, 10)
                print("You try and shoot the Lich with 70% accuracy")
                if arrow <= 7:
                    print("You shoot the Lich and escape the dungeon with many relics.")
                    quit()
                else: print("You try and shoot the lich and miss and then you get melted by the liches magic.")
            else: print("You try and run from the lich but he casts a spell engulfing you in flames.")
            quit()
        else:  print("You head to the right and find a staircase and start to asscend you get to the top and find a chest.\n")  
        princess = input("Do you try and open the chest?y/n\n")
        if princess == "y":
                print("You open the chest expecting great treasures or an enchanted sword, instead it comes alive and eats you")
        else: print("As you are turning around to leave the chest comes alive and eats you")
        quit()
    
       
        response = ""
    elif response == "backward":
            print("coward, leaving an old ruin just because its a bit damp. You should be ashamed")
            quit()
    else:
        print("I didn't understand that.\n")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

