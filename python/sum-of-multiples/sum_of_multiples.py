def sum_of_multiples(limit, multiples):
    unique_multiples = set()
    for number in multiples:
        if number == 0:  
            continue
        for t in range(number, limit, number):
            unique_multiples.add(t)
    return sum(unique_multiples)


result = sum_of_multiples(4, [3, 0])
print(result)
