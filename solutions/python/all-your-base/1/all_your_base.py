def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    zeroes = 0
    for digit in digits:
        if digit == 0:
            zeroes += 1
        if input_base <= digit or digit < 0:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    #print("zeroes: ", zeroes)
    #print("len(digits): ", len(digits))
    if zeroes == len(digits):
        result = [0]
        return result
    number_in_base10 = 0
    current_base = input_base ** (len(digits) - 1)
    for i in range (len(digits)):
        number_in_base10 = number_in_base10 + digits[i] * current_base
        current_base = current_base // input_base
    #print(number_in_base10)
    current_base = output_base
    number_in_output_base = []
    while number_in_base10 > 0:
        number_in_output_base.append( number_in_base10 % output_base)
        number_in_base10 = number_in_base10 // output_base
        current_base = current_base * output_base
    number_in_output_base = number_in_output_base[::-1]
    return number_in_output_base
    #print(number_in_output_base)
rebase(10, [0], 2)