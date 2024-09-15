def reverse(text):
    result = ""
    length = len(text)
    while length > 0:
        result = result + text[length-1]
        length -= 1
    return result
