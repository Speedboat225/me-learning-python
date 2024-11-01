# Identifying integers.

integers = 182849
print(type(integers))

# Identifying strings.

string = "Ping Pong!"
print(type(string))

floats = 3.142
print(type(floats))

boolean = True
print(type(boolean))

# Typecasting.

age=14
print(type(age))

age=str(age)
print("Tyepcasted value ",type(age))

yes = 847
print(type(yes))

yes = float(yes)
print("yes is now a float type!\n", type(yes))

name = input("Enter your name.\n")
print ("Your name is:", name) 

str1="data"
str2="types"
print(str1.join(str2))

items=["apple","banana","orange"]

result=", ".join(items)
print(result)

text="Aarav is learning python"
words=text.split()
print(words)

loganpaul = "I like my cheese drippy bruh"
mold = loganpaul.split()
print(mold)

#neil :-finding length gives u 4
#0  1 2 3

listt=["a","b","c"]
print(len(listt))
print(listt[2])
print(listt[0])

asimpleone = ["The United Kingdom of Great Britain and Northern Ireland", "Indian Ocean", "The old flag of Pocatello in Idaho was horrible.", "Neil", "snek"]
print(asimpleone[:3])#slicing from the start
print(asimpleone[3:])#slice from the end

# to get a set of values with in a range u need to give [start index, end index+1]

a="!dlrow olleH"
print(a[::-1])#reverse

youregettingreversed = input("It would be awesome if you entered some reverse text underneath...\n")
print(youregettingreversed[::-1])