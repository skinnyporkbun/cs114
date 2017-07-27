#Converts gallons to liters and vice versa
print("Would you like to convert gallons to liters? or Liters to gallons")


""" This is the first way, sets the input to a variable and pulls variable later on """
# choice = str(input("Choose here: "))
# if choice == "gallons":
#     print("how many gallons would you like to convert to liters?")
#     g2l = float(input()) * 3.785
#     print (str(g2l) + " liters")
#
# elif choice == "liters":
#     print ("how many liters would you like to convert to gallons?")
#     l2g = float(input())/3.785
#     print (str(l2g) + " gallons")



""" This second way directly checks the input against the arguement to run the else/ifs """
if str(input()) == "gallons":
    print("how many gallons would you like to convert to liters?")
    g2l = float(input()) * 3.785
    print (str(g2l) + " liters")



elif str(input()) == "liters":
    print ("how many liters would you like to convert to gallons?")
    l2g = float(input())/3.785
    print (str(l2g) + " gallons")
