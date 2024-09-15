def slices(series, length):
    if len(series) == 0:
        raise ValueError("series cannot be empty")
    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    result = []
    for i in range(0, len(series) - length + 1):
        newStr = ""
        for j in range(length):
            newStr = newStr + series[i + j]
        result.append(newStr)
    return result
