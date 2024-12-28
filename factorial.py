#7!=7*6*5*4*3*2*1

def factorial():
    fgyu = int(input("number\n"))

    if fgyu==0 or fgyu==1:
        return 1
    else:
        return fgyu*factorial(fgyu-1)
    
    
    
    
    
factorial()
    
    