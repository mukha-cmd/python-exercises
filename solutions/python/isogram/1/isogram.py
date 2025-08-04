def is_isogram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_entries = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    string = string.strip()
    string = string.lower()
    for letter in string:
        if (alphabet.find(letter) != -1):
            alphabet_entries[alphabet.find(letter)] += 1
    for i in range(26):
        if (alphabet_entries[i] >= 2):
            return False
    return True
