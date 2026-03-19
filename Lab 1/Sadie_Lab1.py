# Et tu, Brute?
#
# Team Name: Borq
# Members: Hailey Allman, Sadie Ann, Blair Borque, McKinley Humble, Isaiah Thigpen
# A program that attempts to solve cipher texts that are shifted by some number.

import sys

# the alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\\|;:'\",<.>/? "
ALPHABET_3 = " -,;:!?/.'\"()[]$&#%012345789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxyYzZ" # used on ciphertext3

# STEP 1: read stdin as a string
def txtToString(infile):
    str = ""
    for line in infile:
        str += line
    return str

# STEP 2: get a workable dictionary
def setUpCipherDictionary(str):
    resultingDict = {}
    for i in range(len(str)):
        resultingDict[str[i]] = i
    return resultingDict

# STEP 3: convert cipher into numbers
def cipherToNumber(ciphertext, dictionary):
    result = []
    for i in ciphertext:
        if i in dictionary:
            result.append(dictionary[i])
        else:
            result.append(i)
    return result

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

    #return the sorted version 
#     # return sorted(dict.items(), key=lambda x:x[1],reverse=True)
# print(txtToString("ciphertext-1.txt"))
# print(sorted(frequency_analyzer(txtToString("ciphertext-1.txt")).items(), key=lambda x:x[1],reverse=True))

# for i in range(1, len(ALPHABET)):
    # print("Shift: " + str(i))
    # print(decode(txtToString("ciphertext-1.txt"), i))
    

if __name__ == '__main__':
    Ciphertext = txtToString(sys.stdin)
    CipherDictionary = setUpCipherDictionary(ALPHABET)
    ConvertedCiphertext = cipherToNumber(Ciphertext, CipherDictionary)
    print(ConvertedCiphertext)
