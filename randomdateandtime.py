import random
from datetime import timedelta, datetime

def randimndaertreandtime(start, end):
    start = datetime.fromisoformat(start)
    end = datetime.fromisoformat(end)

    return  start+timedelta(seconds=random.randint(0,int((end-start).total_seconds())))
firstdate = input("enter first date in iso format\n")
seconddate = input("enter second date in iso format\n")
print("heres a randomly selected date between the two:", randimndaertreandtime(firstdate, seconddate))