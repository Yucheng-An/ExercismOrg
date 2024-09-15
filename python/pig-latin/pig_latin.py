def oneWord(word):
    vowels = "aeiou"
    if word[0] in vowels or word.startswith("xr") or word.startswith("yt"):
        return word + "ay"
    qu_index = word.find("qu")
    if qu_index == 0 or (qu_index > 0 and word[0] not in vowels):
        return word[qu_index + 2:] + word[:qu_index + 2] + "ay"
    y_index = word.find("y")
    if y_index > 0 and all(char not in vowels for char in word[:y_index]):
        return word[y_index:] + word[:y_index] + "ay"
    for i, char in enumerate(word):
        if char in vowels:
            return word[i:] + word[:i] + "ay"
    return word + "ay"




def translate(words):
    words = words.split()
    print(words)
    result = ""
    if len(words) == 1:
        return oneWord(words[0])
    else:
        result = oneWord(words[0])
        for i in range(1, len(words) - 1):
            result = result + " " + oneWord(words[i])
        result = result + " " + oneWord(words[len(words) - 1])
    return result
