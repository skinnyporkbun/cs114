print("What is the total price you are paying?")
total = float(input("Total Dollars and cents here: "))

print("How much are you paying the cashier?")
paid = float(input("How much you paid: "))

change = paid - total
print("Your change will be " + str(round(change, 2)))
#
# quarters = int(change//.25)
# print("You will get " + str(round(quarters) + " quarters.")
# newchange = float(change - (quarters*.25))
# print(str(newchange))
