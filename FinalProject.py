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
    Name = ""

class Orc:
    Name = "Orc"
    Health = 20
    Attack = 2
    Defense = 3

class Wolf:
    Name = "Wolf"
    Health = 5
    Attack = 3
    Defense = 1

class Slime:
    Name = "Slime"
    Health = 2
    Attack = 1
    Defense = 1

class Boss:
    Name = "Boss"
    Health = 50
    Attack = 10
    Defense = 10
    Killed = False

# class Environment:
#     enviro = ""

class Misc:
    count = 0
    AmuletGet = False
    TravelCount = 0
#---------------------Independent global variables--------------
plate = 4
leather = 2
cloth = 1

#------------------------ FUNCTIONS FOR CODE------------------

#------Function to set up random enviroment-----
def RandEnv():
    Misc.TravelCount = 0
    random = randint(1,4)
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

def travel(enviro):
    if enviro == "forest":
        Misc.TravelCount += 1
        if Misc.TravelCount == 1:
            print("You start to cautiously enter an ominous forest.")
            TravelDice(enviro)
        elif Misc.TravelCount == 2:
            print("You continue your slow trek through the thick underbrush.")
            TravelDice(enviro)
        elif Misc.TravelCount == 3:
            print("The eerie silence of the forest causes you to ponder about life as you trudge on.")
            TravelDice(enviro)
        elif Misc.TravelCount == 4:
            print("The silence weighs in on you heavily as you walk forward, seeing the glimmer of sunlight as the trees open outwards.")
            enviro = RandEnv()
            return enviro
    elif enviro == "desert":
        Misc.TravelCount += 1
        if Misc.TravelCount == 1:
            print("You step into the sand of a desert with the sun beating down on you.")
            TravelDice(enviro)
        elif Misc.TravelCount == 2:
            print("As you continue forward, a lizard scurries into the cover of a rock to your left side.")
            TravelDice(enviro)
        elif Misc.TravelCount == 3:
            print("Your potions bottles clink against each other, as you thirst for liquids.")
            TravelDice(enviro)
        elif Misc.TravelCount == 4:
            print("Feet dragging in the sand, you come over the top of a sand dune to see a new environment.")
            enviro = RandEnv()
            return enviro
    elif enviro == "plain":
        Misc.TravelCount += 1
        if Misc.TravelCount == 1:
            print("Grasses and grains sway in the open fields in front of you.")
            TravelDice(enviro)
        elif Misc.TravelCount == 2:
            print("Leaving a visible trail behind in the grasses, you walk forward, hoping to get clear of the grass.")
            TravelDice(enviro)
        elif Misc.TravelCount == 3:
            print("A thunderstorm rumbles in the distance of the plains, alerting you of incoming rain.")
            TravelDice(enviro)
        elif Misc.TravelCount == 4:
            print("Sunlight shows itself as you finally reach what you think is the edge of the plain.")
            enviro = RandEnv()
            return enviro
    elif enviro == "savannah":
        Misc.TravelCount += 1
        if Misc.TravelCount == 1:
            print("Dirt crunches under your feet as you walk into the savannah.")
            TravelDice(enviro)
        elif Misc.TravelCount == 2:
            print("You pass countless dead shrubs as you keep a watch out for potential enemies and predators.")
            TravelDice(enviro)
        elif Misc.TravelCount == 3:
            print("Dropping to the ground, you see a saber-toothed cow chasing down a small leohare.")
            TravelDice(enviro)
        elif Misc.TravelCount == 4:
            print("Leaving the dry land behind, you march forward into a new scene.")
            enviro = RandEnv()
            return enviro

def TravelDice(enviro):
    Dice = randint(1, 6)
    if Dice == 1:
        travel(enviro)
    elif Dice == 2:
        travel(enviro)
    elif Dice == 3:
        travel(enviro)
    elif 4 <= Dice <= 6:
        encounter(enviro)

# ---Function to allow player to heal using a potion---
def potion(monster):
    if Player.PotionCount >= 1:
        Player.Health += 5
        if Player.Health > 15:
            Player.Health = 15
        Player.PotionCount -= 1
        print("You've used a potion and recovered to " + str(Player.Health) + " health!")
    else:
        print("You don't have any potions!")
        PlayerTurn(monster)


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

def encounter(enviro):
    Misc.count += 1
    mondice = randint(1,100)
    if Misc.count == 5:
        monster = Boss()
    elif 41 <= mondice <= 80:
        monster = Wolf()
    elif 81 <= mondice <= 100:
        monster = Orc()
    elif 1 <= mondice <= 40:
        monster = Slime()
    if Player.Health > 0:
        if monster.Name == "Orc":
            print("An " + monster.Name + " is attacking!")
        else:
            print("A " + monster.Name + " is attacking!")
    PlayerTurn(monster, enviro)

def PlayerTurn(monster, enviro):
    if Player.Health > 0:
        print("What will you do?")
        print("Attack       Defend")
        print("Potion (" + str(Player.PotionCount) + ")   Flee")
        BattleChoice = input()
        if BattleChoice == "Attack":
            AttackChoice(monster, BattleChoice, enviro)
        elif BattleChoice == "Potion":
            if Player.Health == 15:
                sleep(1)
                print("You're at full health!")
                PlayerTurn(monster, enviro)
            elif Player.Health < 15:
                sleep(1)
                potion(monster)
                MonsterTurn(monster, BattleChoice, enviro)
        elif BattleChoice == "Defend":
            sleep(1)
            print("You block in hopes of weakening " + monster.Name + "\'s Attack!")
            MonsterTurn(monster, BattleChoice, enviro)
        elif BattleChoice == "Flee":
            sleep(1)
            print("You try to run away!")
            FleeChoice(monster, BattleChoice)
        elif BattleChoice == "Kill":
            monster.Health = 0
            AttackChoice(monster, BattleChoice, enviro)
        else:
            sleep(1)
            print("Please make a choice")
            PlayerTurn(monster, enviro)

def MonsterTurn(monster, BattleChoice, enviro):
    if monster.Health > 0:
        miss = randint(1,100)
        if miss < Player.Dodge:
            sleep(1)
            print(monster.Name + " missed it's attack!")
            PlayerTurn(monster, enviro)
        elif miss > Player.Dodge:
            if BattleChoice == "Defend":
                DefendChoice(monster)
                PlayerDeathCheck(monster)
            else:
                Player.Health -= monster.Attack - (Player.Defense//5)
                sleep(1)
                print(monster.Name + " attacked you for " + str(monster.Attack) + " damage!")
                PlayerDeathCheck(monster)

def PlayerDeath(monster):
    print(Player.Name + " was gutted by the " + monster.Name + " in their attempt to find glory and treasures...")
    print("Let this be a lesson to any other adventurers that may pursue the same path...")

def DefendChoice(monster):
    BlockedAttack = monster.Attack//1.5 - (Player.Defense*2)//5
    Player.Health -= int(BlockedAttack)
    print(monster.Name + " attacked you for " + str(int(BlockedAttack)) + " damage!")

def PlayerDeathCheck(monster):
    if Player.Health > 0:
        sleep(1)
        print(str(Player.Health) + " health remaining.")
        PlayerTurn(monster, enviro)
    elif Player.Health <= 0:
        sleep(1)
        print("0 health remaining")
        PlayerDeath(monster)

def FleeChoice(monster, BattleChoice):
    FleeChance = Player.Dodge + randint(1, 70)
    if FleeChance >= 50:
        print("You've managed to slip away from " + monster.Name + ".")
    elif FleeChance <= 49:
        print("You didn't manage to get away from " + monster.Name + ".")
        MonsterTurn(monster, BattleChoice, enviro)

def AttackChoice(monster, BattleChoice, enviro):
            monster.Health -= Player.Attack - (monster.Defense//5)
            print("You attacked " + monster.Name + " for " + str(Player.Attack) + " damage!")
            if monster.Health > 0:
                sleep(1)
                print(monster.Name + " has " + str(monster.Health) + " health remaining!")
                MonsterTurn(monster, BattleChoice, enviro)
            elif monster.Health <= 0:
                sleep(1)
                print(monster.Name + " has been defeated!")
                LootChance(monster)
                travel(enviro)

def EnviroObstacle(enviro):
    if enviro == "forest":
        return "tree"
    elif enviro == "desert":
        return "sand dune"
    elif enviro == "savannah":
        return "dried log"
    elif enviro == "plain":
        return "clump of tall grass"

def LootChance(monster):
    Dice = randint(17, 20)
    if 1 <= Dice <= 10:
        print("You couldn't scavange anything from the " + monster.Name + ".")
    elif 11 <= Dice <= 16:
        print("You found a potion underneath the corpse of " + monster.Name + "!")
        Player.PotionCount += 1
        print("You now have " + str(Player.PotionCount) + " potions.")
    else:
        AmuAttack = randint(0,5)
        AmuDefense = randint(0,5)
        Player.Attack += AmuAttack
        Player.Defense += AmuDefense
        if Misc.AmuletGet == False:
            Misc.AmuletGet = True
            print("You found a magical amulet on the ground nearby!")
            print("You now have " + str(Player.Attack) + " attack and " + str(Player.Defense) + " defense!")
        elif Misc.AmuletGet == True:
            print("You found a magical amulet on the ground nearby!")
            print("The new amulet fuses with the one that you are already wearing!")
            print("You now have " + str(Player.Attack) + " attack and " + str(Player.Defense) + " defense!")

def TravelEncounter():
    enviro = RandEnv()
    travel(enviro)
#-------------------------------------- Textual context. Story and game dialogue.

# print("Adventurers Guild Receptionist: Welcome traveler! You aren't the first to try and challenge the wild forests")
# print("of this area!")
# sleep(0.5)
# print("Adventurers Guild Receptionist: What may I address you as?")
# Player.Name = str(input())
# print("Adventurers Guild Receptionist: Ah, so " + Player.Name + ", you want the glory and treasures of this dark forest?")
# sleep(0.5)
# print("Adventurers Guild Receptionist: You're gonna need some starter gear, as I see that you have nothing with you!")
# sleep(1)
# print("Adventurers Guild Receptionist: Would you like a shortsword and shield, battleaxe, or a bow?")
# weaponselect()
# print("Adventurers Guild Receptionist: You're probably gonna want some armor too.")
# print("Adventurers Guild Receptionist: Would you like the platemail, leather armor, or cloth armor?")
# armorselect()
if Boss.Killed == True:
    print("You've won!")
else:
    TravelEncounter()
