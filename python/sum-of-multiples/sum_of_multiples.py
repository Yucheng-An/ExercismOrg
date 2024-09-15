def sum_of_multiples(limit, multiples):
    test = [1,2,3,4,5,6,7,8,9]
    for i in multiples:
        print(test* i)

    print(test)


asdfasdfasfsadfsafdas

    if len(multiples) == 0:
        return 0
    list1 =[]
    list2 =[]
    for i in multiples:
        if i * 3 < limit:
            list1.append(i*3)
    for i in multiples:
        if i * 5 < limit:
            list2.append(i*5)
    newList = set(list1+list2)
    sum = 0
    for i in newList:
        sum = sum + int(i)
    return sum
print(sum_of_multiples(20, [1,2,3,4,5,6,7]))