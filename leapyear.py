def divcheck(m,n):
    return True if m % n == 0 else False 

#x = int(input("Input: "))

def isLeapyear(x):
    if (divcheck(x,4)):
        if (divcheck(x,100)):
            if (divcheck(x,400)):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        
"""
if (isLeapyear(x) == True):
    print (x, " is a leap year")
else:
    print (x, " is not a leap year")
"""
