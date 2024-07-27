def wordFindSolve(key, string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for letter in string:
        if letter in alphabet:
            letter_index = (alphabet.find(letter) - key) % len(alphabet)
            result = result + alphabet[letter_index]
        else:
            result = result + letter
    return result

file=open("Garmadon's Codes.txt")
lines=file.readlines
for line in lines:
    print(wordFindSolve(13,line))