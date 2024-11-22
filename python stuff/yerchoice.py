print("Program Started.")

# Exam Eligibility Check.

while True:

    medornot = input("To proceed with the examination, do you have a medical cause? (Y/N)\n").upper().strip()

    if medornot == "Y":
        print("You may proceed with the examination.\n")
        break

    elif medornot == "N":
        try:
            attendancerate = int(input("Enter your attendance rate.\n"))

            if attendancerate >= 75:
                print("You may proceed with the examination.\n")
                break

            elif attendancerate < 75:
                print("Sorry, you are not allowed to take this examination!\n")
                break

        except ValueError:
            print("Invalid input, let me ask again:")
    else:
        print("Invalid input, let me ask again:")