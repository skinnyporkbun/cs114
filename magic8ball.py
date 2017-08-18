from random import randint
yeslist = ["Yes", "YES", "yes", "Y", "y"]
nolist = ["No", "NO", "no", "N", "n"]

def magicball():
    if number == 1:
        print("A cookie will fall from the sky and land upon your blessed head, " + name + ".")
    elif number == 2:
        print("You will soon lose something valuable to you, " + name + ". Like your cookie.")
    elif number == 3:
        print("Your day will be great and filled with rightous glory! " + name + ", Go conquer the world!")
    elif number == 4:
        print("Nobody is going to mess with you today, " + name + ". Be Free!")
    elif number == 5:
        print("Major crisis is going to enter your life. Be prepared for anything between zombies and toe stubbing.")
    elif number == 6:
        print("Watch out for cars, " + name + ". They hurt.")
    elif number == 7:
        print("You will soon win a championship in your hobby. You won't get paid though. Sucks to be you " + name + ".")
    elif number == 8:
        print("Many lottery tickets will be bought. None won. Don't do it.")
    else:
        print("You're going to have a pretty normal day, " + name + ". What normal is will be left up to you.")

print("Hey, whats your name?")
name = str(input())
number = randint(1, 9)
magicball()
print("Would you like to run it again?")
yesno = str(input())
if (yesno in yeslist):
    magicball()
elif (yesno in nolist):
    print("Alright, Cya then!")
else:
    print("You\'re speaking gibberish, I'll just stop. Weirdo.")
