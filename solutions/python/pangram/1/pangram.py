def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_entries = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    sentence = sentence.strip()
    sentence = sentence.lower()
    for letter in sentence:
        if (alphabet.find(letter) != -1):
            alphabet_entries[alphabet.find(letter)] += 1
    for i in range(26):
        if (alphabet_entries[i] == 0):
            return False
    return True
