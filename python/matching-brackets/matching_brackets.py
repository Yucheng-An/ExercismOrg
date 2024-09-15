def is_paired(input_string):
    stackList = [0]
    for i in input_string:
        if i == '[' or i == ']' or i == '(' or i == ')' or i == '{' or i == '}':
            if i == '[' or i == '(' or i == '{':
                stackList.append(i)
            elif i == ']' or i == ')' or i == '}':
                if stackList[-1] == "[" and i == ']':
                    stackList.pop(-1)
                elif stackList[-1] == "{" and i == '}':
                    stackList.pop(-1)
                elif stackList[-1] == "(" and i == ')':
                    stackList.pop(-1)
                else:
                    return False
    if len(stackList) == 1:
        return True
    else:
        return False
