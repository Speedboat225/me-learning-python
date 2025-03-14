def square(n):
    return n*n

def addition(n, a):
    return n+a

list1 = [3, 7, 2, 4]
list2 = [4, 9, 8, 1]

addedlists = map(addition, list1, list2)
print(list(addedlists))

normallist = [2, 4, 6, 8]

squaredlist = map(square, normallist)
print(list(squaredlist))

namelist = ["Mike", "Walter", "Gustavo", "Jesse"]
numberlist = [4, 1337, 105901105635774705, 0]

zippedlist = zip(namelist, numberlist)
reversezippedlist = zip(namelist, reversed(numberlist))
print(list(zippedlist))
print("reverse version of previous list:", list(reversezippedlist))
print("dictionary verson of previous list:", dict(zip(namelist, numberlist)))

def countto10butstopat5():
    for i in range(1,11):
        print("Current value is :",i)
        if i == 5:
            exit()

ihatefive = countto10butstopat5()
    

