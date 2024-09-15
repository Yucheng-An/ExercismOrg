def find(search_list, value):
    return binarySearch(search_list, value, 0, len(search_list) - 1)


def binarySearch(search_list, value, low, high):
    if low > high:
        raise ValueError("value not in array")
    mid = (high+low)//2
    if search_list[mid] == value:
        return mid
    elif search_list[mid] > value:
        return binarySearch(search_list, value, low, mid - 1)
    else:
        return binarySearch(search_list, value, mid + 1, high)
