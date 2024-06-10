from Crypto.Cipher import AES
import hashlib
import ast

def pad_msg(message):
    while len(message) % 16 != 0:
        message += b" " 
    return message

def encryption():
    cipher = AES.new(key, mode, iv)
    message = input("Enter Message to Encrypt: ").encode() 
    padded_msg = pad_msg(message)
    encrypt_msg = cipher.encrypt(padded_msg)
    print(encrypt_msg)

def decryption():
    while True:
        try:
            cipher = AES.new(key, mode, iv)
            message = input("Enter Message to Decrypt: ")
            byte_data = ast.literal_eval(message)
            decrypt_msg = cipher.decrypt(byte_data)
            print(decrypt_msg.rstrip().decode())
            break
        except ValueError:
            print("Incorrect key. Please provide the correct key.")
            new_key = input("Enter New Key: ").encode()
            update_key(new_key)

def update_key(new_key):
    global key
    key = hashlib.sha256(new_key).digest()

password = input("Enter Key: ").encode()
key = hashlib.sha256(password).digest()
mode = AES.MODE_CBC
iv = b"1234567890123456"

while True:
    user = input("Encrypt/Decrypt (E/D): ").lower()
    if user == "e":
        encryption()
    elif user == "d":
        decryption()

