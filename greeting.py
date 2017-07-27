# Ask user to input name and age

from time import sleep

print("Hey stranger... Whats your name?")
sleep( 2 )
name = input("What is it? Tell me...hehe...:")

sleep( 1 )

#Ask user to input age
print("And how old are you?")
sleep( 1 )
age = int(input("Tell me, Tell me, I won't hurt you..."))

print("So you're called " + name + " and you're " + str(age) + " years old?")
sleep( 1 )
print("You'll be " + str((age +1)) + " next year then, won'tcha.")

sleep(10)
print("Why are you still here?")
