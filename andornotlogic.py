# AND and OR gate testing.

a = 5
b = 10
c = 15


if a<b and c>b:
    print (True)

else:
    print (False)

d = 5
e = 5
f = 100

if f>d*e or d!=e:
    print(True)

else:
    print (False)

# Not Equal to testing.
    
z = "hi123"
a = "I said no 'hi123', only 'bye456'."

if z!=a:
    print("idk")

else:
    print("ajhahuauhhushuduishui")

# BMI Checker.
    
height=float(input("Yo enter your height! (In Centimetres.)\n"))

weight = float(input("Nah, Imma need your weight too. (In Kilograms.)\n"))

bmi= weight /((height)**2)

print(bmi)

if bmi <= 18.5:
    print("Underweight.")

elif bmi <=24.5:
    print("Normal weight.")

elif bmi > 24.5:
    print("Overweight.")
    
elif bmi >= 30:
    print("Obese.")

