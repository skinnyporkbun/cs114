#Lists to use for if statements to check. As well as list to record data
reminder = []
yeslist = ["Yes", "YES", "yes", "Y", "y"]
nolist = ["No", "NO", "no", "N", "n"]

#Intro to program, asks what users wants to be reminded of
print("Hello! What would you like to be reminded of today?")

#defines function for the program, records data, asks for more data or termination
def todolist():
    #First entry of data recorded, asks for continuation or termination
    print ('Please type out the first thing here: ')
    firstitem = input()
    reminder.append(firstitem)
    print ('Would you like to be reminded of anything else?')
    yesno = input()

    #If statement that checks for user choice of continuation or temrination.
    if (yesno in yeslist):
        print ('What else is it that you would like to remember?')
        todolist()
    elif (yesno in nolist):
        print ('Alright then, here\'s what you still need to do')
    else:
        print ('it broke, please try again.')
        todolist()

#Actual program that runs. starts with Functino todolist, then prints list and ends.
todolist()
print (reminder)
print ("end of block")
