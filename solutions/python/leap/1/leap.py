def leap_year(year):
    if year % 100 != 0:
        if (year % 4 == 0):
            return True
        else:
            return False
    elif year % 400 == 0:
        return True
    else:
        return False
    return False
