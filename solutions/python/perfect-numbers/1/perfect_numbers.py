def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    copy_num = number
    aliquot = 0
    for i in range(1, copy_num):
        if copy_num % i == 0:
            aliquot += i
    if aliquot == copy_num:
        return "perfect"
    elif aliquot < copy_num:
        return ("deficient")
    else:
        return "abundant"
    #classify(15)