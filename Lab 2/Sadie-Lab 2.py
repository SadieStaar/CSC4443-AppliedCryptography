# Le Chiffre
# Team Name: Borq
# Members: Hailey Allman, Sadie Ann, Blair Borque, McKinley Humble, Isaiah Thigpen
# A program that attempts to solve cipher texts that are shifted by some number.
# For the thresholds, we were able to get ciphertext-1= , ciphertext-2= , ciphertext-3= , ciphertext-4= , and the doubly encrypted=

import sys

# the alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\\|;:'\",<.>/? "
ALPHABET_3 = ""
DICTIONARY = {}
REVERSE_DICT = {}
POTENTIAL_KEYS = []
COMMON_WORDS = []

def txtToString(infile):
    str = ""
    for line in infile:
        str += line
    return str

def setUpCipherDictionary(str):
    for i in range(len(str)):
        DICTIONARY[str[i]] = i
        REVERSE_DICT[i] = str[i]

def setUpKeyDictionary(str):
    for i in range(len(str)):
        POTENTIAL_KEYS.append(i)

def setUpCommonWords(dictionaryFile):
    commonWordString = txtToString(open(dictionaryFile, 'r'))
    result = commonWordString.split()
    return result

def cipherToNumber(ciphertext):
    result = []
    for i in ciphertext:
        if i in DICTIONARY:
            result.append(DICTIONARY[i])
        else:
            result.append(i)
    return result

def vignere(ciphertextArray, keyArray):
    rotatedText = ""
    cipherPlace = 0
    keyPlace = 0
    dictlen = len(DICTIONARY)
    try:
        while True:
            if isinstance(ciphertextArray[cipherPlace], int):
                rotatedIndex = (ciphertextArray[cipherPlace] - keyArray[keyPlace] + dictlen) % dictlen
                rotatedText += REVERSE_DICT[rotatedIndex]
                keyPlace = (keyPlace + 1) % len(keyArray)

            else: 
                rotatedText += ciphertextArray[cipherPlace]
            cipherPlace += 1
    except IndexError:
        return rotatedText

def frequencyAnalyzer(decrypted):
    testing = decrypted.lower().split(' ')
    score = 0
    for i in testing:
        if i in COMMON_WORDS: score += 1 
    if score > (len(testing) / 50): return True
    else: return False

if __name__ == '__main__':
    # setup text to be decoded
    setUpCipherDictionary(ALPHABET)
    Ciphertext = txtToString(sys.stdin)
    COMMON_WORDS = setUpCommonWords("./dictionary.txt")
    POTENTIAL_KEYS = setUpCommonWords("./dictionary-1.txt")

    # decode the text
    ConvertedCiphertext = cipherToNumber(Ciphertext)
    testingKey = 0
    while True:
        workingText = vignere(ConvertedCiphertext, cipherToNumber(POTENTIAL_KEYS[testingKey]))
        if (frequencyAnalyzer(workingText)):
            break
        testingKey += 1
    print("Found text:", workingText, "\nkey:", POTENTIAL_KEYS[testingKey])
