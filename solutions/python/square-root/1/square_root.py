def square_root(number):
    if number == 1:
        return number
    for i in range(1, number // 2 + 1):
        if i * i == number:
            return i
    return None