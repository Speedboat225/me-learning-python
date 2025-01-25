emptylist = []
normallist = ["Four is the only number that is spelled with the same number of letters as itself.", "One in 10 people born in Europe are thought to be conceived in an Ikea bed.", "Alaska has a longer coastline than the other 49 states put together."]
reverselist = ["Peter", "Piper", "Picked", "A", "Peck", "Of", "Pickled", "Peppers"]
reverselist = reverselist[::-1]

def Start():
    heloomrmf = str(input("Please enter which list you want to see from the given options: Empty List [E], Normal List [N], Multiplied List [*] or Reversed List [R]\n")).upper().strip()

    if heloomrmf == "E":
        print(emptylist)
        print("(Did you seriously expect something?)")

    elif heloomrmf == "N":
        print(normallist)

    elif heloomrmf == "*":
        multiplicationvalue = int(input("Enter a value to multiply by:\n"))
        multiplicationlist = ["This is the multiplication list."]*multiplicationvalue
        print(multiplicationlist)
    
    elif heloomrmf =="R":
        print(reverselist)

    else:
        print("Looks like you made a typo, restarting...")
        Start()
        
    # Incomplete, not working as intended.

    oeikfdj = (input("Enter some numbers in the following format: [num1], [num2], [num3] and more if you want.\n"))
    oeikfdj = oeikfdj.replace('[', '').replace(']', '').replace(',', '')
    thelistinquestion = list(map(int, oeikfdj.split()))
    
    print(thelistinquestion)

    listsum = sum(thelistinquestion)
    listaverage = listsum / len(thelistinquestion)
    biggestnumber = max(thelistinquestion)
    smallestnumber = min(thelistinquestion)

    print("The sum of the list is:", listsum, "\n The average of the list is:", listaverage, "\n The biggest number in the list is:", biggestnumber, "\n The smallest number in the list is:", smallestnumber)

Start()

