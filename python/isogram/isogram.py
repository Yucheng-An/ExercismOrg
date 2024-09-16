def is_isogram(string):
    alpList = [0] * 26
    for i in string:
        if 97 <= ord(i) <= 122:
            alpList[ord(i) - 97] += 1
        if 65 <= ord(i) <= 90:
            alpList[ord(i) - 65] += 1
    for i in alpList:
        if i >= 2:
            return False
    return True


'''
def is_isogram(string):
    seen = set()
    string = string.lower()
    for char in string:
        if char.isalpha():
            if char in seen:
                return False
            seen.add(char)
    return True
'''
