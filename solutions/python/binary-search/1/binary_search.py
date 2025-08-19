def find(search_list, value):
    left = 0
    right = len(search_list) - 1
    while left <= right:
        middle = (left + right) // 2
        if search_list[middle] == value:
            return middle
        elif search_list[middle] < value:
            left = middle + 1
        elif search_list[middle] > value:
            right = middle - 1
    raise ValueError("value not in array")
#print(find([1, 2, 3, 4, 8, 12, 16, 23, 28, 32], 0))

