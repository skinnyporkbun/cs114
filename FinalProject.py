from time import sleep
swordlist = ["Shortsword", "shortsword", "Shortsword and Shield", "Shortsword and shield", "shortsword and shield", "shield", "sword", "Sword"]
axelist = ["Battleaxe", "battleaxe"]
bowlist = ["Bow", "bow"]
yeslist = ["Yes", "YES", "yes", "Y", "y"]
nolist = ["No", "NO", "no", "N", "n"]
platelist = ["plate", "platemail"]
leatherlist = ["leather", "leather armor"]
clothlist = ["cloth", "cloth armor"]

class Player:
    Health = 15
    Attack = 2
    Defense = 3
    Dodge = 10

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

def potion():
    Player.Health += 5

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
        print("Hey, thats not what I offered you! Pick something!")
        weaponselect()
    print("So, you'll have around " + str(Player.Attack) + " damage as well as " + str(Player.Defense) + " defense!")
    print("Sound good? gimme a yes or no.")
    yesno = str(input())
    if (yesno in yeslist):
        print("Alrighty then, continuing onwards then.")
    elif (yesno in nolist):
        print("Okay then, tell me what you really want!")
        Player.Health = 15
        Player.Attack = 2
        Player.Defense = 3
        weaponselect()

def armorselect():
    playerarmor = str(input())
    if (playerarmor in platelist):
        Player.Defense += 4
    elif (playerarmor in leatherlist):
        Player.Defense += 2
    elif (playerarmor in clothlist):
        Player.Defense += 1
        Player.Dodge += 20
    else:
        print("Hey, stop being silly, pick something")
        armorselect()
    if (playerarmor in clothlist):
        print("Okay so you have " + str(Player.Defense) + " and " + str(Player.Dodge) + "% chance to avoid monsters.")

print("Welcome traveler! You aren't the first to try and challenge the wild forests")
print("of this area!")
sleep(1)
print("What may I addres you as?")
PlayerName = str(input())
print("Ah, so " + PlayerName + ", you want the glory and treasures of this dark forest?")
sleep(1)
print("You're gonna need some starter gear, as I see that you have nothing with you!")
sleep(1)
print("Would you like a shortsword and shield, battleaxe, or a bow?")
weaponselect()
print("You're probably gonna want some armor too.")
print("Would you like the platemail, leather armor, or cloth armor?")
armorselect()
