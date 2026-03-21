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

def txtToString(infile):
    str = ""
    for line in infile:
        str += line
    return str

def setUpCipherDictionary(str):
    for i in range(len(str)):
        DICTIONARY[str[i]] = i

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
    for i in range(0, len(numArray)):
        if isinstance(numArray[i], int):
            numArray[i] = (int(numArray[i]) + rotation) % dictLen
    return numArray

def frequency_analyzer(str):
    dict = {}
    for c in str:
        if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
            c = c.lower()
        
        if(dict.get(c) != None):
                dict[c] +=1
        else:
            dict[c] = 1
    
    return dict
    
if __name__ == '__main__':
    # setup text to be decoded
    setUpCipherDictionary(ALPHABET)
    Ciphertext = txtToString(sys.stdin)

    # decode the text
    ConvertedCiphertext = cipherToNumber(Ciphertext)
    print(ConvertedCiphertext)
    print(rotate(ConvertedCiphertext, 3))
