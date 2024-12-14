# character occurence

#word ="john"
#word[0]
#word[1]
#word[i]==char

word = input("hi enter a word or sentence\n")
char = input("now enter a character\n")

i = 0
o = 0

while i <len(word):
    if word[i]==char:
        o=o+1
    i=i+1
print("the amount of times", char, "appears in", word, "is equal to:", o)

# prime numbers

num = int(input("hi enter a number pls\n"))
num2 = int(input("another one (but bigger)\n"))

print("prime numbers between", num, "and", num2, "are:",)

for num3 in range(num, num2+1):
    if num3 > 1:
        for a_variable in range(2, num3):
            if (num3%a_variable)==0:
                break

        else:
            print(num3)

input("")

# micdle number