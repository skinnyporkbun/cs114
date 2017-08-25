from time import sleep
from random import randint

#------------------------------Lists for possible options of player response-----------
swordlist = ["Shortsword", "shortsword", "Shortsword and Shield", "Shortsword and shield",
"shortsword and shield", "shield", "sword", "Sword", "Shield"]
axelist = ["Battleaxe", "battleaxe"]
bowlist = ["Bow", "bow"]
yeslist = ["Yes", "YES", "yes", "Y", "y"]
nolist = ["No", "NO", "no", "N", "n"]
platelist = ["plate", "platemail", "Platemail", "Plate"]
leatherlist = ["leather", "leather armor", "Leather", "Leather armor", "Leather Armor"]
clothlist = ["cloth", "cloth armor", "Cloth Armor", "Cloth"]


#-----------------------------Classes for units inside of game----------
class Player:
    Health = 15
    Attack = 2
    Defense = 3
    Dodge = 10
    PotionCount = 2

class Orc:
    mobtype = "Monster"
    Health = 20
    Attack = 2
    Defense = 3

class Wolf:
    mobtype = "Monster"
    Health = 5
    Attack = 3
    Defense = 1

class Slime:
    mobtype = "Monster"
    Health = 2
    Attack = 1
    Defense = 1

class Boss:
    mobtype = "Monster"
    Health = 50
    Attack = 10
    Defense = 10

class Environment:
    enviro = ""

class Monster:
    count = 0

#---------------------Independent global variables--------------
plate = 4
leather = 2
cloth = 1

#------------------------ FUNCTIONS FOR CODE------------------

#------Function to set up random enviroment-----
def RandEnv():
    random = randint(1,1)
    if random == 1:
        enviro = "forest"
        return enviro
    elif random == 2:
        enviro = "desert"
        return enviro
    elif random == 3:
        enviro = "plain"
        return enviro
    elif random == 4:
        enviro = "savannah"
        return enviro


#-----Function for to display different dialogue for each "movement" in terrain, or -------
#reset for new terrain
# def travel():
#
#     if enviro == "forest":
#         forestcount += 1
#         if forestcount == 1:
#             print("You start to cautiously enter an ominous forest.")
#         elif forestcount == 2:
#             print("You continue your slow trek through the thick underbrush.")
#         elif forestcount >= 3:
#             print("The eerie silence of the forest causes you to ponder about life as you trudge on.")
#     elif enviro == "desert":
#         desertcount += 1
#     elif enviro == "plain":
#         plaincount += 1
#     elif enviro == "savannah":
#         savannahcount += 1


# ---Function to allow player to heal using a potion---
def potion():
    if Player.PotionCount >= 1:
        Player.Health += 5
        Player.PotionCount -= 1
        print("You've used a potion and recovered 5 health!")
    else:
        print("You don't have any potions!")


#Function for selecting weapons as well as checking. and Statistics---
def weaponselect():
    playerweapon = str(input())
    if (playerweapon in swordlist):
        Player.Attack += 4
        Player.Defense += 3
    elif (playerweapon in axelist):
        Player.Attack += 5
    elif (playerweapon in bowlist):
        Player.Attack += 8
        Player.Defense -= 2
    else:
        print("Adventurers Guild Receptionist: Hey, thats not what I offered you! Pick something!")
        weaponselect()

    #Code to continue with weapon select
    print("Adventurers Guild Receptionist: So, you'll have around " + str(Player.Attack) + " damage as well as " + str(Player.Defense) + " defense!")
    print("Adventurers Guild Receptionist: Sound good? gimme a yes or no.")
    yesno = str(input())
    if (yesno in yeslist):
        print("Adventurers Guild Receptionist: Alrighty then, continuing onwards then.")
    elif (yesno in nolist):
        print("Adventurers Guild Receptionist: Okay then, tell me what you really want!")
        Player.Health = 15
        Player.Attack = 2
        Player.Defense = 3
        weaponselect()


#Function for selecting armor type as well as their statistics.----
def armorselect():
    #Code for player selecting armor
    playerarmor = str(input())
    if (playerarmor in platelist):
        Player.Defense += plate
    elif (playerarmor in leatherlist):
        Player.Defense += leather
    elif (playerarmor in clothlist):
        Player.Defense += cloth
        Player.Dodge += 20
    else:
        print("Adventurers Guild Receptionist: Hey, stop being silly, pick something")
        armorselect()

    #Code to continue after player selects, including final check
    if (playerarmor in clothlist):
        print("Adventurers Guild Receptionist: Okay so you have " + str(Player.Defense) + " defense and " + str(Player.Dodge) +
        "% chance to evade monsters. That sound good?")
    else:
        print("Adventurers Guild Receptionist: Alright, so you have " + str(Player.Defense) + " defense. Does that sound good to you?")
    yesno2 = str(input())
    if (yesno2 in yeslist):
        print("Adventurers Guild Receptionist: Okay! You better get going then so that you don't lose out on the loot.")
    elif (yesno2 in nolist):
        Player.Dodge = 10
        if (playerarmor in platelist):
            Player.Defense -= plate
        elif (playerarmor in leatherlist):
            Player.Defense -= leather
        elif (playerarmor in clothlist):
            Player.Defense -= cloth
            Player.Dodge -= 20
        print("Adventurers Guild Receptionist: Well, please let me know what it is you want now. Platemail, leather armor, or cloth armor?")
        armorselect()

def encounter():
    Monster.count += 1
    mondice = randint(1,100)
    if 1 <= mondice <= 40:
        print("slime")
    elif 41 <= mondice <= 70:
        print("wolf")
    elif 71 <= mondice <= 95:
        print("orc")
    elif 96 <= mondice <= 100:
        print("boss")
    print(Monster.count)
#-------------------------------------- Textual context. Story and game dialogue.

# print("Adventurers Guild Receptionist: Welcome traveler! You aren't the first to try and challenge the wild forests")
# print("of this area!")
# sleep(0.5)
# print("Adventurers Guild Receptionist: What may I address you as?")
# PlayerName = str(input())
# print("Adventurers Guild Receptionist: Ah, so " + PlayerName + ", you want the glory and treasures of this dark forest?")
# sleep(0.5)
# print("Adventurers Guild Receptionist: You're gonna need some starter gear, as I see that you have nothing with you!")
# sleep(1)
# print("Adventurers Guild Receptionist: Would you like a shortsword and shield, battleaxe, or a bow?")
# weaponselect()
# print("Adventurers Guild Receptionist: You're probably gonna want some armor too.")
# print("Adventurers Guild Receptionist: Would you like the platemail, leather armor, or cloth armor?")
# armorselect()
enviro = RandEnv()
print("As you travel out of the town, you approach a " + enviro + " region.")
print("You start to enter the " + enviro + " on foot and walk at a leisurely pace.")
encounter()
encounter()
encounter()
encounter()

# Potion code
# print("Use potion?")
# usepotion = str(input())
# if (usepotion in yeslist):
#     potion()
# elif (usepotion in nolist):
#     print("You didn't do anything.")
# else:
#     print("Not valid command.")
#
# print(str(Player.Health))
# print("You have " + str(Player.PotionCount) + " potions remaining.")
