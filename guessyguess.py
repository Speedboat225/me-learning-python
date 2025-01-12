import random

playing = True

kka = str(random.randint(0,100))

print("guess a number from 0-100.")

while playing:
    theinputinquestioncolon = input("")

    if theinputinquestioncolon == kka:
        print("you win!!1!!!11!1")
        break

    elif theinputinquestioncolon >= kka:
        print("youre above the number.")
    
    elif theinputinquestioncolon <= kka:
        print("youre under the number.")