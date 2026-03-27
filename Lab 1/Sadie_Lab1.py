# Et tu, Brute?
#
# Team Name: Borq
# Members: Hailey Allman, Sadie Ann, Blair Borque, McKinley Humble, Isaiah Thigpen
# A program that attempts to solve cipher texts that are shifted by some number.

import sys

# Global variables setup
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\\|;:'\",<.>/? "
ALPHABET_3 = " -,;:!?/.'\"()[]$&#%012345789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxyYzZ" # used on ciphertext3
DICTIONARY = {}
REVERSE_DICT = {}
COMMON_WORDS = []

# TEXT TO STRING: Takes in a text file and converts the whole file into one long string for processing
def txtToString(infile):
    str = ""
    for line in infile:
        str += line
    return str

# SET UP CIPHER DICTIONARY: Sets up a value-to-character dictionary for string conversion later.
# also sets up a reverse dictionary to save on iterations for future reconversion
def setUpCipherDictionary(str):
    for i in range(len(str)):
        DICTIONARY[str[i]] = i
        REVERSE_DICT[i] = str[i]

# SET UP COMMON WORDS: takes a file of commonly used english words and converts it into an array; used for frequency testing
def setUpCommonWords(dictionaryFile):
    commonWordString = txtToString(open(dictionaryFile, 'r'))
    result = commonWordString.split()
    return result

# CIPHER TO NUMBER: converts a string of ciphertext into an array of it's value equivalent using the dictionaries from earlier
def cipherToNumber(ciphertext):
    result = []
    for i in ciphertext:
        if i in DICTIONARY:
            result.append(DICTIONARY[i])
        else:
            result.append(i)
    return result

# ROTATE: arithmetic function that 'rotates' each character value by a certain rotation value
# accounts for both overflow and underflow values
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

# FREQUENCY ANALYZER: turns the decrypted string into an array, and compares its elements with common words
# then, a score is generated to decide if the deciphered text is the potential plaintext
def frequencyAnalyzer(decrypted):
    testing = decrypted.lower().split(' ')
    score = 0
    for i in testing:
        if i in COMMON_WORDS: score += 1 
    if score > (len(testing) / 50): return True
    else: return False

# MAIN FUNCTION
if __name__ == '__main__':
    # setup text to be decoded
    setUpCipherDictionary(ALPHABET)
    Ciphertext = txtToString(sys.stdin)
    COMMON_WORDS = setUpCommonWords("./dictionary.txt")

    # decode the text
    ConvertedCiphertext = cipherToNumber(Ciphertext)
    rotations = 0
    while True:
        # iterate the rotation, then rerotate the original values
        rotations = rotations + 1
        workingText = rotate(ConvertedCiphertext, rotations)
        
        # check if what was processed looks like plain english
        if (frequencyAnalyzer(workingText)):
            break
    
    print("Shift of " + str(rotations) + ":\n" + workingText )
