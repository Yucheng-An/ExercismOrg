def is_armstrong_number(number):
    digit = len(str(number))
    numberAsString = str(number)
    result = 0
    for i in numberAsString:
        result += int(i) ** digit
    return result == number
