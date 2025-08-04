def rotate(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_text = ""
    capitals = False
    if (text.isupper()):
        text = text.lower()
        capitals = True
    temp_lower = ""
    for char in text:
        if char.isalpha():
            if (char.isupper()):
                temp_lower = char.lower()
                index = alphabet.find(temp_lower)
                new_text += alphabet[(index + key) % 26].upper()
            else:
                index = alphabet.find(char)
                char = alphabet[(index + key) % 26]
                new_text += char
        else:
            new_text += char
    if (capitals):
        new_text = new_text.upper()
    return new_text