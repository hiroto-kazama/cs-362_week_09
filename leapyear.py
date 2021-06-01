def divcheck(m,n):
    return True if m % n == 0 else False 

#x = int(input("Input: "))

def isLeapyear(x):
    if (divcheck(x,4)):
        return True
    else:
        return False
        
"""
if (isLeapyear(x) == True):
    print (x, " is a leap year")
else:
    print (x, " is not a leap year")
"""
