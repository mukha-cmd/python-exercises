def translate_word(text):
    text_copy = text
    consonants = ""
    vowels = ("a","e","i","o","u","xr","yt")
    # Rule 1
    if text.startswith(vowels):
        text_copy += "ay"
    # Rule 2
    else:
        # now uses a tuple of prefixes instead of separate args
        while text_copy.startswith(vowels) == False:
            if text_copy.startswith("y") and consonants != "":
                break
            consonants += text_copy[0]
            text_copy = text_copy[1:]
        if text_copy.startswith("y"):
            text_copy += consonants
            text_copy += "ay"
        elif text_copy.startswith("u") == True and consonants.endswith("q") == True:
            text_copy = text_copy[1:]
            text_copy += (consonants + "u")
            text_copy += "ay"
        else:
            text_copy += consonants
            text_copy += "ay"
    return text_copy
def translate(text):
    # split on whitespace, translate each, re-join
    words = text.split()
    pigged = [translate_word(w) for w in words]
    return " ".join(pigged)
print(translate("my"))