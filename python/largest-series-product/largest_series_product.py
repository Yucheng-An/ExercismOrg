def largest_product(series, size):
    if len(series) < size:
        raise ValueError("span must be smaller than string length")
    if size <= 0:
        raise ValueError("span must not be negative")
    for i in series:
        if i not in "1234567890":
            raise ValueError("digits input must only contain digits")
    # start analyze
    resultList = []
    for i in range(0,len(series)-size+1):
        res = ''
        for j in range(size):
            res = res + series[i+j]
        resultList.append(res)
    resultList2 = []
    for i in resultList:
        production = 1
        for j in i:
            production = production * int(j)
        resultList2.append(production)
    print(resultList)
    print(resultList2)
    maxNumber = resultList2[0]
    for i in resultList2:
        if maxNumber < i:
            maxNumber = i
    print(maxNumber)
    print(type(maxNumber))
    return maxNumber



largest_product("293221", 2)
