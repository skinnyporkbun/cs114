print ("Hello world")
time.sleep( 2 )
print ("How are you feeling today from 1 to 10? 1 being bad and 10 being good.")
time.sleep( 3 )
feeling = int(input("Tell me here: "))


if 0 < feeling <= 5:
    print ("Aww, well that sucks. Hope you feel better")

else:
    if 6 <= feeling <= 10:
        print ("Well you seem be having a wonderful day! Hope it stays that way!")

print ("Was a pleasure to hear about your day. Unfortunately, I'll be shutting down now so I'll be seeing you around!")
import time
time.sleep( 5 )
exit()
