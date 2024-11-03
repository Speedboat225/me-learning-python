def Start():
    posorneg = int(input("Type a number, can be negative or positive.\n"))

    if posorneg < 0:
        print("Your number is negative.\n")
        Start()
    elif posorneg == 0:
        print("bruh")
        return
    else:
        print("Your number is positive.\n")
        Start()
Start()