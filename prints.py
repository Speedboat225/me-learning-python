import keyword
print ("Hello World!")
print (54)
print ("!dlroW olleH\n")
print ("World Hello!", 54)
print ("Python is pretty cool.", end = " !olleH dlroW")

#Variables


first_name="Neil"
print(first_name)


number=1236
print(number)

# use to take value from the user
#int is for type casting converting one data type into another
num1=int(input("Enter the number here: "))


num2=int(input("Ok great, now enter your battery percentage: "))

sum=num1+num2

print (sum)

school = input("What's the name of your school?\n")

print(school, "huh? Anyways time for some more maths!!! Multiplication.")

num3=int(input("Enter the first number here: "))

num4=int(input("Enter the second number here: "))

sum2=num3*num4

print (sum2, "Congratulations! You did it!\n")

# List of keywords.

print ("The keywords of Python are:\n")

print (keyword.kwlist)