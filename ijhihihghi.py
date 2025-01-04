try:
    hiififif = float(input("enter a number, no cheating this time.\n"))
    print("k cool thx")
except ValueError:
    print("what did i just say?")

try:
    jf = int(input("Enter a number.\n"))
    kf = int(input("Another one.\n"))
    print("Your final number is...",jf/kf)
except ValueError:
    print("bruh")
except ZeroDivisionError:
    print("bruh")
finally:
    print("Fun Fact: “Forty” is the only number that is spelt with letters arranged in alphabetical order.")

try:
    scared = int(input("Enter a number, please not one divisible by two!\n"))

    if scared%2==0:
        while scared:
            print ("Bye.")
    else:
        print("Thank you!")
except ValueError:
    print("bru")