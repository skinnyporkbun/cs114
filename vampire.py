from time import sleep
print("Hey human! How old are you?")
age = input()
if int(age) <= 20 :
    print("Wow, you're a young human.")

elif 21 <= int(age) <= 110:
    print("Wow, kinda old. Still human though.")
elif int(age) >= 111:
    print("Holy smokes, You're too old to be human! I'm gonna grab my wooden stake!")
    sleep(2)
    print("GET AWAY FROM ME! AAGGHHHH")
else:
    print("Hey, you're speaking gibberish. Tell me how old you are.")
    sleep(1)
    print("Else I'll stab you with this stake anyway.")
