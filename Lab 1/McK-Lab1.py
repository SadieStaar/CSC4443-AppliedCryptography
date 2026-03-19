# Et tu, Brute?
#
# Team Name: Borq
# Members: Hailey Allman, Sadie Ann, Blair Borque, McKinley Humble, Isaiah Thigpen
# A program that attempts to solve cipher texts that are shifted by some number.


# imports
from nltk.corpus import words

# the alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\\|;:'\",<.>/? "

# NEW plan: read cipher into a long string, iterate brute force the message, 



# read the file into a single string variable
with open("ciphertext-1.txt", "r") as file:
    ciphertext = file.read()


# shift through all rots, checking the substring until " " a dictionary word is found


#get rot
int x=True
int rot_shift=0
curr_alph = ALPHABET

while (x):
    curr_alph = curr_alph[1:] + curr_alph[0]
    rot_shift++

    if (ciphertext[0] == curr_alph[0]):
        x=False


decrypt_text = ""

# get each letter's index within the constant alphabet
# add the shift rot to it
# mod with alphabet length
# replace the letter with whatever is at that new index

while(y<rot_shift):
    
    


#firstWord = ""

#firstSpace = " "

#firstWord = ciphertext.split(firstSpace)[0]



# test

print(ciphertext)
print()
#print(firstWord)

