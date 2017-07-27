from time import sleep

print ("Hello world")
sleep( 2 )

print ("How are you feeling today from 1 to 10? 1 being bad and 10 being good.")
sleep( 3 )

feeling = int(input("Tell me here: "))

#loop the code if user gives invalid number
while ( 10 < feeling or feeling < 0  ):
    print( "Oi, Oi! I said between 1 and 10 man. Tell me for real this time!" )
    feeling = int(input("Tell me here: "))
# elif 0 < feeling <= 5:
#     print( "Aww, well that sucks. Hope you feel better")
# else:
#     print( "Well you seem to be having a wonderful day.")
# """ Supposed to check the input of user to proceed and/or repeat the input"""
# def today():
#
#         if 0 < feeling <= 5:
#                 print ("Aww, well that sucks. Hope you feel better")
#         elif 6 <= feeling <= 10:
#             print ("Well you seem be having a wonderful day! Hope it stays that way!")
#         elif feeling >= 11:
#             print ("Oi, Oi! I said between 1 and 10 man. Tell me for real this time!")


sleep( 3 )
print ("Unfortunately, I'll be shutting down now so I'll be seeing you around!")
sleep( 5 )

print("HELLO FUTURE ME :D - Voicemail left on Thursday, July 20th, 2017")
