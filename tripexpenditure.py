import datetime

def tibetanmonkmoyaimoyaimoyai(days,hotelcostperday,planeticket,vehiclecost):
    tc = days*hotelcostperday
    tvc = days*vehiclecost
    trip = planeticket+tc+tvc
    
    return trip

days = int(input("How many days?\n"))
hotelcostperday = int(input("Cost of hotel per each day?\n"))
vehiclecost = int(input("Cost of the vehicle per day?\n"))
planeticket = int(input("And finally, cost of the flight ticket?\n"))

print("The total cost of your trip is:", tibetanmonkmoyaimoyaimoyai(days,hotelcostperday,planeticket,vehiclecost))