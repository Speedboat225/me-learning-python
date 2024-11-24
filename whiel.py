

fwgyww = int(input("hi enter a natural number pls\n"))

sum = 0#initialization
i = 1#initialization

while i<=fwgyww:#condition
    sum=sum+i#body of the loop
    i=i+1#increment
    print("\n Sum: ",sum)

# infinity loop thing

icantthinkofanyvariablenames = 0
uiuuhiuih = input("hi ur about to get forkbombed do u want to do it or not (Y/N)\n").upper().strip()
if uiuuhiuih == "Y":
    while icantthinkofanyvariablenames<=0:
        print("i am too lazy to think of a good idea on what to put here")

elif uiuuhiuih == "N":
    print("ok lets do the next part of this program\n")

else:
    while icantthinkofanyvariablenames<=0:
        print("ok you made a typo or tried to trick me im doing it anyways")

# senator armstrong number thing

senatorarmstrong = int(input("hi tell numbers pls\n"))

zero=0
temp=senatorarmstrong

while temp>0:
    digit=temp%10
    zero += digit**3
    temp//=10
if senatorarmstrong==zero:
    print("armstrong")
else:
    print("not an armstrong")

