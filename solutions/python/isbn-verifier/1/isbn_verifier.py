def is_valid(isbn):
    isValidSum = 0
    counter = 10
    numberOfDigits = 0
    for char in isbn:
        if char.isdigit():
            numberOfDigits += 1
    if numberOfDigits > 10 or (numberOfDigits < 10 and isbn.endswith("X") == False):
        return False
    else:
        for char in isbn:
            if char != "-":
                if char != "X":
                    if not char.isdigit():
                        return False
                    else:
                        isValidSum += int(char) * counter
                        counter -= 1
                else:
                    isValidSum += 10
    return isValidSum % 11 == 0