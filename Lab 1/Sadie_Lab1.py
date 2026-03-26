# Et tu, Brute?
#
# Team Name: Borq
# Members: Hailey Allman, Sadie Ann, Blair Borque, McKinley Humble, Isaiah Thigpen
# A program that attempts to solve cipher texts that are shifted by some number.

import sys

# the alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\\|;:'\",<.>/? "
ALPHABET_3 = " -,;:!?/.'\"()[]$&#%012345789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxyYzZ" # used on ciphertext3
DICTIONARY = {}
REVERSE_DICT = {}
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

def rotate(numArray, rotation):
    dictLen = len(DICTIONARY)
    rotatedText = ""
    for i in range(len(numArray)):
        if isinstance(numArray[i], int):
            rotatedIndex = (numArray[i] - rotation + dictLen) % dictLen
            rotatedText += REVERSE_DICT[rotatedIndex]
        else:
            rotatedText += numArray[i]
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

    # decode the text
    ConvertedCiphertext = cipherToNumber(Ciphertext)
    rotations = 0
    while True:
        rotations = rotations + 1
        workingText = rotate(ConvertedCiphertext, rotations)
        if (frequencyAnalyzer(workingText)):
            break
    print("Shift of " + str(rotations) + ":\n" + workingText )
