def fizzBuzz():
    i = 1
    s = ""
    while i < 101:

        if i%3 == 0:
            s += "Fizz "
        elif i%5 == 0:
            s += "Buzz "
        elif i%3 != 0 and i%5 != 0:
            s += str(i)
            s += " "
        i += 1
    return s


print(fizzBuzz())
