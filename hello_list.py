from time import sleep

print ("Hello world")
sleep( 2 )
print ("How are you feeling today from 1 to 10? 1 being bad and 10 being good.")
feeling = input("Tell me here: ")

# if feeling == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10":

if feeling == "skip":
       print("Oh, okay. I won't ask you again then")
elif 0 < int(feeling) <= 5:
    print ("Aww, well that sucks. Hope you feel better")
elif 6 <= int(feeling) <= 10:
        print ("Well you seem be having a wonderful day! Hope it stays that way!")

# if feeling == "skip":
#         print("Oh, okay. I won't ask you again then")




sleep( 3 )
print ("Unfortunately, I'll be shutting down now so I'll be seeing you around!")
sleep( 5 )

print("HELLO FUTURE ME :D - Voicemail left on Thursday, July 20th, 2017")
