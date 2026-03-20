# Lab 1: Et tu, Brute?
# Team Name: Borq
# Members: Hailey Allman, Sadie Ann, Blair Borque, McKinley Humble, Isaiah Thigpen
# A program that attempts to solve cipher texts that are shifted by some number.


# the alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "

ciphertext = input("Enter the cipher text: ")


def loadDict(file):
     with open(file, 'r') as f:
          return set(word.strip().lower() for word in f)
     

def decode(str, shift):
        decoded = ""
        for c in str:
            
            if ALPHABET.find(c) != -1:
                decoded += ALPHABET[(ALPHABET.find(c) + shift) % len(ALPHABET)]
            else:
                decoded += c
        return decoded

def isValid(str, dictionary):
    words = str.split()
    if not words:
        return False

    valid = 0
    for w in words:
         w_clean = ''.join(ch for ch in w if ch.isalpha()).lower()
         if w_clean in dictionary:
              valid += 1

    return valid / len(words) > 0.5

dictionary = loadDict("dictionary.txt")


# try all possible shifts and check if the decoded text is valid
for shift in range(len(ALPHABET)):
     candidate = decode(ciphertext, shift)

     if isValid(candidate, dictionary):
        print(f"Likely shift: {shift}")
        print(f"Decoded text: {candidate}")
        break
else: print("This shi broke ;-;")