def calculateMinefield(minefield, row, column, i, j):
    # Go up
    if i != 0 and minefield[i - 1][j] != '*':
        minefield[i - 1][j] = minefield[i - 1][j] + 1
    # Go down
    if i != row - 1 and minefield[i + 1][j] != '*':
        minefield[i + 1][j] = minefield[i + 1][j] + 1
    # Go right
    if j != column - 1 and minefield[i][j + 1] != '*':
        minefield[i][j + 1] = minefield[i][j + 1] + 1
    # Go left
    if j != 0 and minefield[i][j - 1] != '*':
        minefield[i][j - 1] = minefield[i][j - 1] + 1
    # Go up-right
    if i != 0 and j != column - 1 and minefield[i - 1][j + 1] != '*':
        minefield[i - 1][j + 1] = minefield[i - 1][j + 1] + 1
    # Go down-right
    if i != row - 1 and j != column - 1 and minefield[i + 1][j + 1] != '*':
        minefield[i + 1][j + 1] = minefield[i + 1][j + 1] + 1
        # Go up-left
    if i != 0 and j != 0 and minefield[i - 1][j - 1] != '*':
        minefield[i - 1][j - 1] = minefield[i - 1][j - 1] + 1
    # Go down-left
    if i != row - 1 and j != 0 and minefield[i + 1][j - 1] != '*':
        minefield[i + 1][j - 1] = minefield[i + 1][j - 1] + 1


def checkValid(minefield):
    column = len(minefield[0])
    for i in minefield:
        if column != len(i):
            raise ValueError("The board is invalid with current input.")
        for j in i:
            if 65 <= ord(j) <= 90 or 97 <= ord(j) <= 122:
                raise ValueError("The board is invalid with current input.")


def annotate(minefield):
    if len(minefield) == 0:
        return []
    if len(minefield[0]) == "":
        return [""]
    checkValid(minefield)
    tempList = []
    for row in minefield:
        tempList.append(list(row))
    row = len(minefield)
    column = len(minefield[0])

    minefield = tempList
    for i in range(0, row):
        for j in range(0, column):
            if minefield[i][j] == " ":
                minefield[i][j] = 0
    for i in range(0, row):
        for j in range(0, column):
            if minefield[i][j] == "*":
                calculateMinefield(minefield, row, column, i, j)
    result = []
    for i in range(0, row):
        t = ""
        for j in range(0, column):
            if minefield[i][j] == 0:
                minefield[i][j] = " "
                t = t + str(minefield[i][j])
            else:
                t = t + str(minefield[i][j])
        result.append(t)
    return result
