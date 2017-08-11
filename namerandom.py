yeslist = ["Yes", "YES", "yes", "Y", "y"]
nolist = ["No", "NO", "no", "N", "n"]
import sys
from random import randint
from time import sleep
def restart():
    print("You wanna new name?")
    yesno = input()
    if (yesno in yeslist):
        print("Okay!")
        sleep(1)
        name()
    elif (yesno in nolist):
        print("Okay, See you next time then!")
        sys.exit()
def name():
    print("Here! Have a name!")
    namenumber = randint(1,5)
    if namenumber == 1:
        print("Your new name is Joe!")
        restart()
    elif namenumber == 2:
        print("Your new name is Jill!")
        restart()
    elif namenumber == 3:
        print("Your name is now Andre!")
        restart()
    elif namenumber == 4:
        print("Your name is gonna be Nathan now.")
        restart()
    elif namenumber == 5:
        print("Your name is Wakawaka Chicken Thing")
        restart()

name()
