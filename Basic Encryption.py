import random 
import string 

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)


def encryption():
    plain_text  = input("Enter Message encrypt: ")
    cipher_text = ""

    for ind in plain_text:
        index = chars.index(ind)
        cipher_text += key[index]

    print(cipher_text)

def dncryption():
    cipher_text  = input("Enter Message to decrypt: ")
    plain_text = ""

    for ind in cipher_text:
        index = key.index(ind)
        plain_text += chars[index]

    print(plain_text)



while True:
    user = input("Encrypt/Decrypt?\n").lower()
    if user == "e":
        encryption()
    elif user == "d":
        dncryption()