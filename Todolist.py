reminder = []

print ("Hello! What would you like to remember today?")
print ("Please type out the first thing here: ")
reminder.append(input(str()))

print ("Would you like to be reminded of anything else?")
yesno = str(input())

# Create a loop to continue asking for more whilst user says YES and stop when user says NO
# loopcheck = 0
# while loopcheck == 0:
#
if str(yesno) == "Yes" or "YES" or "yes" or "y" or "Y":
    print ("What else is it that you would like to remember?")
    reminder.append(input(str()))
    print ("Would you like to be reminded of anything else? Yes or no?")
elif str(yesno) == "No" or "NO" or "no" or "n" or "N":
    print ("Alright then, here's what you still need to do")
# else:
#     print ("it broke")

# if yesno == "No" or "NO" or "no" or "n" or "N":
#     print ("OKAY BYE")
print (reminder)
