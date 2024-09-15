def is_valid(isbn):
    givingStr = isbn.replace("-", "")
    print(givingStr)
    print(len(givingStr))
    if len(givingStr) != 10:
        return False
    j = 10
    sum = 0
    for i in range(0, 10):
        if i == 9 and givingStr[i] == 'X':
            sum = sum + 10 * j
            j -= 1
        elif 48 <= ord(givingStr[i]) <= 57:
            sum = sum + int(givingStr[i]) * j
            j -= 1
        else:
            return False
    print(sum)
    if sum % 11 == 0:
        return True
    else:
        return False

