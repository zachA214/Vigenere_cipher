import sys

# encrypt_vigenere, decrypt_vigenere, and generate key functions provided by https://www.geeksforgeeks.org/vigenere-cipher/

def check_python_version():
    print("Detecting Python version")
    # Check if the Python version is 3.x
    if sys.version_info[0] < 3:
        raise EnvironmentError("This script requires Python 3.x or higher. Please upgrade your Python version.")
    else:
        print("Python 3.x detected. Proceeding...")

def within_range(value, upperbound, lowerbound):
    if(value <= upperbound and value >= lowerbound):
        return True
    return False

def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(msg, key):
    encrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)
    return "".join(encrypted_text)

def decrypt_vigenere(msg, key):
    decrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)


plaintext = ""
ciphertext = ""
key = ""

check_python_version()

print("Project Name ------- Author --------- Last Update")
print("Vigenere Cipher -- Zachary Adelson -- Feb 18th 2025")

print("1. Decrypt with key")
print("2. Decrypt without key")
print("3. Encrypt")
menuOption = input("Select Option ")

# Input validation, check if user input is within range and loop if not
while(menuOption.isdigit(menuOption) and menuOption):
    key_check = input(key_check + " is not a valid input, please enter y/n ")
print("ok you said " + key_check)


ciphertext = encrypt_vigenere(plaintext, key)
print(f"Encrypted Text: {ciphertext}")

plaintext = decrypt_vigenere(ciphertext, key)
print(f"Decrypted Text: {plaintext}")