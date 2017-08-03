print("What is the total price you are paying?")
total = float(input("Total Dollars and cents here: "))

print("How much are you paying the cashier?")
paid = float(input("How much you paid: "))

change = paid - total
print("Your change will be " + str(round(change, 2)))

quarters = int(change//.25)
if quarters > 1 or quarters == 0:
    print("You will get " + str(quarters) + " quarters,")
else:
    print("You will get " + str(quarters) + " quarter,")
newchange = float(round(change - (quarters*.25), 2))

dimes = int(newchange//.10)
if dimes > 1 or dimes == 0:
    print("and " + str(dimes) + " dimes,")
else:
    print("and " + str(dimes) + " dime,")
change = float(round(newchange - (dimes*.1), 2))

nickels = int(change//.05)
if nickels > 1 or nickels == 0:
    print ("and " + str(nickels) + " nickels,")
else:
    print ("and " + str(nickels) + " nickel,")
newchange = float(round(change - (nickels*.05), 2))

pennies = int(newchange//.01)
if pennies > 1 or pennies == 0:
    print ("and " + str(pennies) + " pennies.")
else:
    print ("and " + str(pennies) + " penny.")
