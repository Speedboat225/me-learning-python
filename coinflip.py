import random
def fjjfke():

    list1=["tails","heads"]

    computerschoice = random.choice(list1)

    hi = random.randint(1,2)
    if hi == 1:
        correctchoice = "heads"

    elif hi == 2:
        correctchoice = "tails"

    while True:

        userschoice = input("Choose either heads or tails.\n").lower().strip()

        if userschoice == computerschoice:
            print("You said the same thing as me, restarting..")
            fjjfke()

        elif userschoice == "heads" and computerschoice == "tails" and correctchoice == "heads":
            print("You win.")
            break

        elif userschoice == "tails" and computerschoice == "heads" and correctchoice == "tails":
            print("You win.")
            break

        elif userschoice == "heads" and computerschoice == "tails" and correctchoice == "tails":
            print("I win.")
            break

        elif userschoice == "tails" and computerschoice == "heads" and correctchoice == "heads":
            print("I win.")
            break

fjjfke()