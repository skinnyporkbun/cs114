from random import randint
yeslist = ["Yes", "YES", "yes", "Y", "y"]
nolist = ["No", "NO", "no", "N", "n"]


def get_responselist():
    responseList = ["A cookie will fall from the sky and land upon your blessed head, name.",
"You will soon lose something valuable to you, name. Like your cookie.",
"Your day will be great and filled with rightous glory! name, Go conquer the world!",
"Nobody is going to mess with you today, name. Be Free!",
"Major crisis is going to enter your life. Be prepared for anything between zombies and toe stubbing.",
"Watch out for cars, name. They hurt.",
"You will soon win a championship in your hobby. You won't get paid though. Sucks to be you name.",
"Many lottery tickets will be bought. None won. Don't do it.",
"You're going to have a pretty normal day, name. What normal is will be left up to you."
]
    return responseList

# def magicball(number, name):
#     if number == 1:
#         print("A cookie will fall from the sky and land upon your blessed head, " + name + ".")
#     elif number == 2:
#         print("You will soon lose something valuable to you, " + name + ". Like your cookie.")
#     elif number == 3:
#         print("Your day will be great and filled with rightous glory! " + name + ", Go conquer the world!")
#     elif number == 4:
#         print("Nobody is going to mess with you today, " + name + ". Be Free!")
#     elif number == 5:
#         print("Major crisis is going to enter your life. Be prepared for anything between zombies and toe stubbing.")
#     elif number == 6:
#         print("Watch out for cars, " + name + ". They hurt.")
#     elif number == 7:
#         print("You will soon win a championship in your hobby. You won't get paid though. Sucks to be you " + name + ".")
#     elif number == 8:
#         print("Many lottery tickets will be bought. None won. Don't do it.")
#     elif number == 9:
#         print("You're going to have a pretty normal day, " + name + ". What normal is will be left up to you.")



def magicball2(number, name):
    if number == 1:
        response = responseList[0]
        response.replace("name", name)
        return response
    elif number == 2:
        response = responseList[1]
        response.replace("name", name)
        return response
    elif number == 3:
        response = responseList[2]
        response.replace("name", name)
        return response
    elif number == 4:
        response = responseList[3]
        response.replace("name", name)
        return response
    elif number == 5:
        response = responseList[4]
        response.replace("name", name)
        return response
    elif number == 6:
        response = responseList[5]
        response.replace("name", name)
        return response
    elif number == 7:
        response = responseList[6]
        response.replace("name", name)
        return response
    elif number == 8:
        response = responseList[7]
        response.replace("name", name)
        return response
    elif number == 9:
        response = responseList[8]
        response.replace("name", name)
        return response

def promptname():
    print("Hey, whats your name?")
    name = str(input())
    return name

def randnum(listsize):
    number = randint(1, listsize)
    return number

def rerun(name):
    print("Would you like to run it again?")
    yesno = str(input())
    if (yesno in yeslist):
        number = randnum(listsize)
        response = magicball2(number, name)
        print(response)
        rerun(name)
    elif (yesno in nolist):
        print("Alright, Cya then!")
    else:
        print("You\'re speaking gibberish, I'll just stop. Weirdo.")

def Main():
    responseList = get_responselist()
    listsize = len(responseList)
    number = randnum(listsize)
    name = promptname()
    response = magicball2(number, name)
    print (response)
    rerun(name)

Main()
