# The start function is allowing the program to restart.

def start():

    # Beginning of the program.

        print ("Program Started.")
        print ("This program requires 5 birth dates.\n")

    # Getting the birthdates and storing them in variables.
        birthdate1 = input ("Please enter the first birthdate:\n")
        birthdate2 = input ("Please enter the second birthdate:\n")
        birthdate3 = input ("Please enter the third birthdate:\n")
        birthdate4 = input ("Please enter the fourth birthdate:\n")
        birthdate5 = input ("Please enter the fifth birthdate:\n")

    # Allowing the user to verify if they have entered the correct birthdates.

        print ("Birthdates received, the following birthdates you have entered are:\n")

        print("Birthdate 1:", birthdate1)
        print("Birthdate 2:", birthdate2)
        print("Birthdate 3:", birthdate3)
        print("Birthdate 4:", birthdate4)
        print("Birthdate 5:", birthdate5)

    # The thing actually letting them verify.

        confirmation = input("Are the following birthdates correct? (Y/N)\n")

        if confirmation.upper() == "Y":
            print("Birthdates accepted, thank you!")
            return
        if confirmation.upper() == "N":
            print("Restarting the program, please review your inputs carefully.\n")
            start()
        else:
            print("Invalid response, Restarting the program...\n")
            start()

start()

