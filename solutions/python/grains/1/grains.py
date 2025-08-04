def square(number):
    if (number < 1 or number > 64):
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    initial = 1
    final = 0
    for i in range(1, 65):
        final += initial
        initial *= 2
    return final
