def is_armstrong_number(number):
    number_of_digits = 0
    copy_number = number
    flag = number
    total = 0
    while (copy_number >= 1):
        copy_number = copy_number // 10
        number_of_digits += 1
    while (number >= 1):
        total = total + (number % 10) ** number_of_digits
        number = (number // 10)
    if (flag == total):
        return True
    else:
        return False