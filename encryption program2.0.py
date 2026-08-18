import random
import string

word = string.punctuation + string.digits + string.ascii_letters
word = list(word)
#print(word)

#print()
key = word.copy()
random.shuffle(key)
#print(key)



text = input("enter your text to encrypt:- ")
encrypt_text = ""

for letter in text:
    index = word.index(letter)
    encrypt_text += key[index]



print(f"your test is:- {text}  ")
print(f"your encrypt_text is :- {encrypt_text}")
