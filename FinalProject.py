from time import sleep
from random import randint

""" Lists for input option checks """
swordlist = ["Shortsword", "shortsword", "Shortsword and Shield", "Shortsword and shield",
"shortsword and shield", "shield", "sword", "Sword", "Shield"]
axelist = ["Battleaxe", "battleaxe", "Axe", "axe"]
bowlist = ["Bow", "bow"]
yeslist = ["Yes", "YES", "yes", "Y", "y"]
nolist = ["No", "NO", "no", "N", "n"]
platelist = ["plate", "platemail", "Platemail", "Plate"]
leatherlist = ["leather", "leather armor", "Leather", "Leather armor", "Leather Armor"]
clothlist = ["cloth", "cloth armor", "Cloth Armor", "Cloth"]
SSkillList = ["Flurry Swipe", "Block and Stab"]
ASkillList = ["Wide Swing", "Power Swing"]
BSkillList = ["Multi-Shot", "Focus"]

""" Class list for entities in the game """
class Player:
    Health = 15
    Attack = 2
    Defense = 3
    Dodge = 10
    PotionCount = 2
    Name = ""
    Weapon = ""

class Orc:
    Name = "Orc"
    Health = 20
    Attack = 5
    Defense = 8

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

class Misc:
    count = 0
    AmuletGet = False
    TravelCount = 0
    CD1Count = 0
    CD2Count = 0
    Focus = False

""" Global Variables """
plate = 4
leather = 2
cloth = 1
enviro = ""
#------------------------ FUNCTIONS FOR CODE------------------


""" Travel and Encounter Functions """
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
#-----reset for new terrain
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

#---Dice function for whether player moves or encounters a monster
def TravelDice(enviro):
    Dice = randint(1, 6)
    RandomTime = randint(2, 4)
    if Dice == 1:
        sleep(RandomTime)
        travel(enviro)
    elif Dice == 2:
        sleep(RandomTime)
        travel(enviro)
    elif Dice == 3:
        sleep(RandomTime)
        travel(enviro)
    elif 4 <= Dice <= 6:
        sleep(RandomTime)
        encounter(enviro)

#---Runs functions to do encounters and movement. Basically wrap for every movement function
def TravelEncounter():
    enviro = RandEnv()
    travel(enviro)

#---Dice and count check for which monster is encounter when an encounter occurs
def encounter(enviro):
    Misc.count += 1
    mondice = randint(1,100)
    if Misc.count == 7:
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


""" Functions for Start of game """
#Function for selecting weapons as well as checking. and Statistics---
def weaponselect():
    playerweapon = str(input())
    if (playerweapon in swordlist):
        Player.Attack += 4
        Player.Defense += 3
        Player.Weapon = "sword"
    elif (playerweapon in axelist):
        Player.Attack += 5
        Player.Weapon = "axe"
    elif (playerweapon in bowlist):
        Player.Attack += 8
        Player.Defense -= 2
        Player.Weapon = "bow"
    else:
        print("Adventurers Guild Receptionist: Hey, thats not what I offered you! Pick something!")
        weaponselect()

    #Code to continue with weapon select
    print("Adventurers Guild Receptionist: So, you'll have around " + str(Player.Attack) + " damage as well as " + str(Player.Defense) + " defense!")
    sleep(3.5)
    print("Adventurers Guild Receptionist: Sound good? gimme a yes or no.")
    yesno = str(input())
    if (yesno in yeslist):
        sleep(2)
        print("Adventurers Guild Receptionist: Alrighty then, continuing onwards then.")
    elif (yesno in nolist):
        sleep(1)
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
        sleep(2)
        print("Adventurers Guild Receptionist: Okay so you have " + str(Player.Defense) + " defense and " + str(Player.Dodge) +
        "% chance to evade monsters. That sound good?")
    else:
        sleep(2)
        print("Adventurers Guild Receptionist: Alright, so you have " + str(Player.Defense) + " defense. Does that sound good to you?")
    yesno2 = str(input())
    if (yesno2 in yeslist):
        sleep(3)
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
        sleep(2)
        print("Adventurers Guild Receptionist: Well, please let me know what it is you want now. Platemail, leather armor, or cloth armor?")
        armorselect()


""" Player Combat Functions """

#---Function that allows player's choices. Attack, Defend, Potion, Flee
def PlayerTurn(monster, enviro):
    if Player.Health > 0:
        if Misc.Focus == True:
            BattleChoice = ""
            Misc.Focus = False
            print("You fire off your shot after focusing.")
            SwingDmg = Player.Attack + 5
            monster.Health -= SwingDmg
            print("Your shot did " + str(SwingDmg) + " to " + monster.Name + "!")
            MonDeath(monster, BattleChoice, enviro)
        else:
            print("What will you do?")
            print("Attack  Skill  Defend")
            print(" Potion (" + str(Player.PotionCount) + ")   Flee ")
            BattleChoice = input()
            if BattleChoice == "Attack":
                AttackChoice(monster, BattleChoice, enviro)
            elif BattleChoice == "Potion":
                if Player.Health == 15:
                    sleep(2)
                    print("You're at full health!")
                    PlayerTurn(monster, enviro)
                elif Player.Health < 15:
                    sleep(2)
                    potion(monster)
                    MonsterTurn(monster, BattleChoice, enviro)
            elif BattleChoice == "Defend":
                sleep(2)
                print("You block in hopes of weakening " + monster.Name + "\'s Attack!")
                MonsterTurn(monster, BattleChoice, enviro)
            elif BattleChoice == "Flee":
                sleep(2)
                print("You try to run away!")
                FleeChoice(monster, BattleChoice)
            elif BattleChoice == "Skill":
                print("Which skill would you like to use?")
                SkillList(monster, BattleChoice, enviro)
            else:
                sleep(2)
                print("Please make a choice")
                PlayerTurn(monster, enviro)

#---Function that runs player's damage formula when attacking or if monster dies
def AttackChoice(monster, BattleChoice, enviro):
    SwingDmg = Player.Attack - (monster.Defense//5)
    monster.Health -= SwingDmg
    print("You attacked " + monster.Name + " for " + str(SwingDmg) + " damage!")
    if monster.Health > 0:
        sleep(1)
        print(monster.Name + " has " + str(monster.Health) + " health remaining!")
        MonsterTurn(monster, BattleChoice, enviro)
    elif monster.Health <= 0:
        MonDeath(monster, BattleChoice, enviro)

#---Function that runs formula for defending against a monster's attack
def DefendChoice(monster):
    BlockedAttack = monster.Attack//1.5 - (Player.Defense*2)//5
    if BlockedAttack > 0:
        Player.Health -= int(BlockedAttack)
        sleep(2)
        print(monster.Name + " attacked you for " + str(int(BlockedAttack)) + " damage!")
    elif BlockedAttack <= 0:
        print("You've deflected the attack!")

#---Shows the skill list based on weapon for the player upon selection
def SkillChoice(monster, BattleChoice, enviro):
    if Player.Weapon == "sword":
        CDText()
    elif Player.Weapon == "axe":
        CDText()
    elif Player.Weapon == "bow":
        CDText()
    SkillCast(monster, BattleChoice, enviro)

#---Function to allow player to heal using a potion---
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

#---Function that checks whether the player successfully flees from the battle
def FleeChoice(monster, BattleChoice):
    FleeChance = Player.Dodge + randint(1, 70)
    if FleeChance >= 50:
        print("You've managed to slip away from " + monster.Name + ".")
        sleep(2)
    elif FleeChance <= 49:
        print("You didn't manage to get away from " + monster.Name + ".")
        sleep(2)
        MonsterTurn(monster, BattleChoice, enviro)

#---Contains all the specifics for the skills and weapon types.
def SkillCast(monster, BattleChoice, enviro):
    Cast = input()
    if Player.Weapon == "sword":
        if Cast == "Flurry Swipe":
            if Misc.CD1Count > 0:
                print("This skill is on cooldown!")
                PlayerTurn(monster, enviro)
            elif Misc.CD1Count <= 0:
                Misc.CD1Count += 2
                print("You swing your sword wildly at the enemy!")
                SwingDmg = (Player.Attack//1.5) - (monster.Defense//5)
                monster.Health -= SwingDmg
                print("You swing once dealing " + str(int(SwingDmg)) + " damage!")
                monster.Health -= SwingDmg
                print("You swing a second time dealing " + str(int(SwingDmg)) + " damage!")
                MonDeath(monster, BattleChoice, enviro)
        elif Cast == "Block and Stab":
            if Misc.CD2Count > 0:
                print("This skills is on cooldown!")
                PlayerTurn(monster, enviro)
            elif Misc.CD2Count <= 0:
                Misc.CD2Count += 4
                SwingDmg = Player.Attack - (monster.Defense//5)
                monster.Health -= SwingDmg
                if monster.Health > 0:
                    print("You stab at " + monster.Name + " and raise your shield to guard afterwards.")
                    print("You attacked for " + str(int(SwingDmg)) + " damage!")
                    print(monster.Name + " has " + str(int(monster.Health)) + " remaining.")
                    print("You are now defending.")
                    BattleChoice = "Defend"
                    MonsterTurn(monster, BattleChoice, enviro)
                elif monster.Health <= 0:
                    sleep(1)
                    print(monster.Name + " has been defeated!")
                    if monster.Name == "Boss":
                        Boss.Killed = True
                    else:
                        LootChance(monster)
                        travel(enviro)

        elif Cast == "Cancel":
            print("Returning to player menu.")
            PlayerTurn(monster, enviro)
        else:
            print("Please choose a skill or Cancel.")
            SkillList(monster, BattleChoice, enviro)
    elif Player.Weapon == "axe":
        if Cast == "Wide Swing":
            if Misc.CD1Count > 0:
                print("This skill is on cooldown!")
                PlayerTurn(monster, enviro)
            elif Misc.CD1Count <= 0:
                Misc.CD1Count += 2
                print("You do a wide sweep in front of you with your axe.")
                SwingDmg = Player.Attack - (monster.Defense//6)
                monster.Health -= SwingDmg
                print("You did " + str(SwingDmg) + " damage to " + monster.Name + ".")
                if monster.Health > 0:
                    print(monster.Name + " has " + str(int(monster.Health)) + " health remaining!")
                    StunDice = randint(1, 10)
                    if StunDice > 6:
                        print(monster.Name + " was stunned by your attack!")
                        PlayerTurn(monster, enviro)
                    else:
                        MonsterTurn(monster, BattleChoice, enviro)
        if Cast == "Power Swing":
            if Misc.CD2Count > 0:
                print("This skill is on cooldown!")
                PlayerTurn(monster, enviro)
            elif Misc.CD2Count <= 0:
                Misc.CD2Count += 3
                print("You cleave downwards with all your strength")
                SwingDmg = Player.Attack
                monster.Health -= Player.Attack
                print("You struck " + monster.Name + " for " + str(SwingDmg) + " damage!")
                MonDeath(monster, BattleChoice, enviro)
        elif Cast == "Cancel":
            print("Returning to player menu.")
            PlayerTurn(monster, enviro)
        else:
            print("Please choose a skill or Cancel.")
            SkillList(monster, BattleChoice, enviro)
    elif Player.Weapon == "bow":
        if Cast == "Multi-Shot":
            if Misc.CD1Count > 0:
                print("This skill is on cooldown!")
                PlayerTurn(monster, enviro)
            elif Misc.CD1Count <= 0:
                Misc.CD1Count += 3
                print("You fire a barrage of arrows quickly at " + monster.Name + ".")
                SwingDmg = (Player.Attack//1.85) - monster.Defense//4
                monster.Health -= SwingDmg*5
                print(monster.Name + " was shot for " + str(int(SwingDmg)) + " damage!")
                print(monster.Name + " was shot for " + str(int(SwingDmg)) + " damage!")
                print(monster.Name + " was shot for " + str(int(SwingDmg)) + " damage!")
                print(monster.Name + " was shot for " + str(int(SwingDmg)) + " damage!")
                print(monster.Name + " was shot for " + str(int(SwingDmg)) + " damage!")
                MonDeath(monster, BattleChoice, enviro)
        if Cast == "Focus":
            if Misc.CD2Count > 0:
                print("This skill is on cooldown!")
                PlayerTurn(monster, enviro)
            elif Misc.CD2Count <= 0:
                Misc.CD2Count += 3
                print("You focus, listening to your surroundings and controlling your breathing.")
                Misc.Focus = True
                MonDeath(monster, BattleChoice, enviro)
        elif Cast == "Cancel":
            print("Returning to player menu.")
            PlayerTurn(monster, enviro)
        else:
            print("Please choose a skill or Cancel.")
            SkillList(monster, BattleChoice, enviro)

""" Combat Functions"""

#---Function that checks for monster missing an attack or hitting player
def MonsterTurn(monster, BattleChoice, enviro):
    if monster.Health > 0:
        miss = randint(1,100)
        Misc.CD1Count -= 1
        Misc.CD2Count -= 1
        if miss < Player.Dodge:
            sleep(2)
            print(monster.Name + " missed it's attack!")
            PlayerTurn(monster, enviro)
        elif miss > Player.Dodge:
            if BattleChoice == "Defend":
                DefendChoice(monster)
                PlayerDeathCheck(monster)
            else:
                MonDmg = monster.Attack - (Player.Defense//5)
                Player.Health -= MonDmg
                sleep(2)
                print(monster.Name + " attacked you for " + str(MonDmg) + " damage!")
                PlayerDeathCheck(monster)

#---Function that checks if player has any health left or is dead
def PlayerDeathCheck(monster):
    if Player.Health > 0:
        sleep(2)
        print(str(Player.Health) + " health remaining.")
        PlayerTurn(monster, enviro)
    elif Player.Health <= 0:
        sleep(2)
        print("0 health remaining")
        PlayerDeath(monster)

#---Function that checks for loot when monster dies
def LootChance(monster):
    Dice = randint(1, 20)
    if 1 <= Dice <= 10:
        print("You couldn't scavange anything from the " + monster.Name + ".")
    elif 11 <= Dice <= 16:
        print("You found a potion underneath the corpse of " + monster.Name + "!")
        Player.PotionCount += 1
        print("You now have " + str(Player.PotionCount) + " potions.")
    else:
        AmuletFormula()
        AmuletText()

#---Monster Death check
def MonDeath(monster, BattleChoice, enviro):
    if monster.Health > 0:
        sleep(1)
        print(monster.Name + " has " + str(int(monster.Health)) + " health remaining!")
        MonsterTurn(monster, BattleChoice, enviro)
    elif monster.Health <= 0:
        sleep(1)
        print(monster.Name + " has been defeated!")
        if monster.Name == "Boss":
            Boss.Killed = True
        else:
            LootChance(monster)
            travel(enviro)


""" Amulet Functions """

def AmuletFormula():
    AmuAttack = randint(0,5)
    AmuDefense = randint(0,5)
    Player.Attack += AmuAttack
    Player.Defense += AmuDefense

def AmuletText():
    if Misc.AmuletGet == False:
        Misc.AmuletGet = True
        print("You found a magical amulet on the ground nearby!")
        sleep(1)
        print("You now have " + str(Player.Attack) + " attack and " + str(Player.Defense) + " defense!")
    elif Misc.AmuletGet == True:
        print("You found a magical amulet on the ground nearby!")
        sleep(1)
        print("The new amulet fuses with the one that you are already wearing!")
        sleep(1)
        print("You now have " + str(Player.Attack) + " attack and " + str(Player.Defense) + " defense!")

""" Text Functions """

#---Function that displays text when player dies
def PlayerDeath(monster):
    sleep(3)
    print(Player.Name + " was gutted by the " + monster.Name + " in their attempt to find glory and treasures...")
    sleep(3)
    print("Let this be a lesson to any other adventurers that may pursue the same path...")
    quit()

#--- Function that controls what text prints for cooldown and the skill list
def CDText():
    skill1 = SSkillList[0]
    skill2 = SSkillList[1]
    if Misc.CD1Count > 1:
        Cd1 = Misc.CD1Count-1
    else:
        Cd1 = Misc.CD1Count
    if Misc.CD2Count > 1:
        Cd2 = Misc.CD2Count-1
    else:
        Cd2 = Misc.CD2Count
    if Cd1 <=0 and Cd2 <= 0:
        print(skill1 + "(0), " + skill2 + "(0)")
    elif Cd1 <= 0:
        print(skill1 + "(0), " + skill2 + "(" + str(Cd2) + ")")
    elif Cd2 <= 0:
        print(skill1+ "(" + str(Cd1) + ")" + skill2 + "(0)")
    else:
        print(skill1 + "(" + str(Cd1) + "), " + skill2 + "(" + str(Cd2) + ")")

#--- Function that runs all the intro text as well as the weapon and armor select.
def Intro():
    print("Adventurers Guild Receptionist: Welcome traveler! You aren't the first to try and challenge the wild forests")
    print("of this area!")
    sleep(2)
    print("Adventurers Guild Receptionist: What may I address you as?")
    Player.Name = str(input())
    sleep(0.5)
    print("Adventurers Guild Receptionist: Ah, so " + Player.Name + ", you want the glory and treasures of this dark forest?")
    sleep(3)
    print("Adventurers Guild Receptionist: You're gonna need some starter gear, as I see that you have nothing with you!")
    sleep(2)
    print("Adventurers Guild Receptionist: Would you like a shortsword and shield, battleaxe, or a bow?")
    weaponselect()
    sleep(0.5)
    print("Adventurers Guild Receptionist: You're probably gonna want some armor too.")
    sleep(2)
    print("Adventurers Guild Receptionist: Would you like the platemail, leather armor, or cloth armor?")
    armorselect()
    sleep(0.5)

#---Function that runs text once you beat the game.
def WinText():
    print("  After the defeating the \"Boss\", you decide that you have had enough")
    sleep(1)
    print("                 of the adventuring business.")
    sleep(1)
    print("As the years go on, stories of the adventurer who killed the local terror")
    print("                           \"Boss\",")
    print("       will be passed down as a legend. The story of " + Player.Name + "...")

""" Main Function """

def Main():
    Intro()
    while Boss.Killed == False:
        TravelEncounter()
    WinText()

#------- Runs game
Main()
