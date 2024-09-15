def square(number):
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        if number == 1:
            return number
        else:
            base = 2
            for i in range(1,number-1):
                base = base * 2
            return base



def total():
    temp = 0
    for i in range(64):
        temp = temp + square(i+1)
    return temp
