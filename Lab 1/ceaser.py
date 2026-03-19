# Lab 1: Et tu, Brute?
# Team Name: Borq
# Members: Hailey Allman, Sadie Ann, Blair Borque, McKinley Humble, Isaiah Thigpen
# A program that attempts to solve cipher texts that are shifted by some number.


# the alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\\|;:'\",<.>/? "

def txtToString(file): # takes in a file and returns the contents as a string
    f = open(file, "r") # opens the file in read mode
    str = f.read()
    
    f.close()
    return str

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

def decode(str, shift):
        decoded = ""
        for c in str:
            if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
                c = c.lower()
            
            if ALPHABET.find(c) != -1:
                decoded += ALPHABET[(ALPHABET.find(c) + shift) % len(ALPHABET)]
            else:
                decoded += c
        return decoded
     

    #return the sorted version 
#     # return sorted(dict.items(), key=lambda x:x[1],reverse=True)
# print(txtToString("ciphertext-1.txt"))
# print(sorted(frequency_analyzer(txtToString("ciphertext-1.txt")).items(), key=lambda x:x[1],reverse=True))

for i in range(1, len(ALPHABET)):
    print("Shift: " + str(i))
    print(decode(txtToString("ciphertext-1.txt"), i))
    