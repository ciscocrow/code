print("""You Enter a dark room with two doors.
Do you go through door #1 or door#2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good Job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")
elif door == "2":
    print("""
    You Stare into the endless abyss at Cthulha's retna.
    1. Blueberries
    2. Yellow jacket clothespins.
    3. Understanding revolvers yelling melodies. """)

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("the insanity rots your eyes into a pool of muck.")
        print("good job")
elif door == "3":
    print("There was no door 3")
else:
    print("you stumble around and fall on a kinfe and die. Good job!")
