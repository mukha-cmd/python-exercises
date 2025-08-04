def response(hey_bob):
    reply_striped = hey_bob.strip()
    if (reply_striped == ""):
        return "Fine. Be that way!"
    all_capitals = False
    letter_count = 0
    upper_count = 0
    for char in reply_striped:
        if char.isalpha():
            letter_count += 1
            if char.isupper():
                upper_count += 1
    is_question = reply_striped.endswith("?")
    if (letter_count > 0 and letter_count == upper_count):
        all_capitals = True
    else:
        all_capitals = False
    if (is_question == True and all_capitals == False):
        return "Sure."
    elif (is_question == True and all_capitals == True):
        return "Calm down, I know what I'm doing!"
    elif (is_question == False and all_capitals == True):
        return "Whoa, chill out!"
    return "Whatever."
