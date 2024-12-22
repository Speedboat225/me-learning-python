def well_wishes(name):
    print("Hello",name,"How are you?")


well_wishes("Neil!")

def season(s):
    spring = "nice"
    summer = "hot"
    autumn = "nice"
    winter = "cold"

    if s=="winter":
        print("The season is pretty" ,winter)

    elif s=="spring":
        print("The season is pretty" ,spring)

    elif s=="summer":
        print("The season is pretty" ,summer)

    elif s=="autumn":
        print("The season is pretty" ,autumn)

    

s = input("hi what is season\n")

season(s)


def addition(q,w):
    return q+w

def division(q,w):
    return q/w

def subtraction(q,w):
    return q-w

def multiplication(q,w):
    return q*w

print("Please select the operation u want:")
print("A. addition")
print("B. subtraction")
print("C. division")
print("D. multiplication")

choice=input("Please enter your choice(A, B, C or D)").upper().strip()
num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

if choice == "A":
    print(addition(num_1,num_2))
if choice == "B":
    print(subtraction(num_1,num_2))
if choice == "C":
    print(division(num_1,num_2))
if choice == "D":
    print(multiplication(num_1,num_2))




















