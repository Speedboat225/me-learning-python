# Cool Is operator test!

maybefive = int(input("hi enter a number equal to 5 or not\n"))

five = 5

print(maybefive is five)


# Extremely cool bitwise operator test...

leftorright = input("You a leftie or a rightie? (L/R)\n").upper()

if leftorright == "L":
    leftie = int(input("Enter a number, can be negative or positive I don't care.\n"))
    print("Doubling your number for being a leftie becomes:", leftie<<1)

if leftorright == "R":
    rightie = int(input("Enter a number, can be negative or positive I don't care.\n"))
    print("Halving your number for being a rightie becomes:", rightie>>1)

# your grades.
    
math = int(input("Enter your Math grades, now.\n"))
science = int(input("You thought that was it? Give your Science grades as well.\n"))
english = int(input("By the hest of Henry VIII, it is a necessity to ent'r thy English grades.\n"))
computerscience = int(input("Enter your Computer Science grades or your computer will go kaboom!\n"))
geography = int(input("Enter your Geography grades or I will send a nuclear bomb to your address\n"))

resultsfiguring = (math + science + english + computerscience + geography)/5

print("The average of your marks are:", resultsfiguring)

if resultsfiguring >= 90:
    print("You got an A Grade, be happy you live another day.")

elif resultsfiguring < 90 and resultsfiguring >= 75:
    print("B Grade stands for be better, now.")

elif resultsfiguring < 75 and resultsfiguring >= 60:
    print("C Grade stands for can you survive for a minute to win $1?")

elif resultsfiguring < 60 and resultsfiguring >= 46:
    print("D Grade stands for do something to make up for it, or else...")

elif resultsfiguring <= 45:
    print("F Grade stands for FATALITY.")
