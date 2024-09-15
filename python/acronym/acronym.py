def abbreviate(words):
    for char in "-,._":
        words = words.replace(char, " ")
    wordsList = words.split()
    print(wordsList)
    result = ''
    for i in wordsList:
        if 96 <= ord(i[0]) <= 96 + 26:
            result += chr(ord(i[0]) - 32)
        elif 65 <= ord(i[0]) <= 65 + 26:
            result += i[0]
    return result
