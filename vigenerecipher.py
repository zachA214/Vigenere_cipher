import sys

def check_python_version():
    print("Detecting Python version")
    # Check if the Python version is 3.x
    if sys.version_info[0] < 3:
        raise EnvironmentError("This script requires Python 3.x or higher. Please upgrade your Python version.")
    else:
        print("Python 3.x detected. Proceeding...")

def within_range(value, lowerbound, upperbound):
    if value <= upperbound and value >= lowerbound:
        return True
    return False

def vingenere_encrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_length = len(key)
    ciphertext = ciphertext.upper()
    keyIndex = 0 #this is here because using i to determine shift
    #gets messed up because of the existence of many spaces
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[keyIndex % key_length]) - ord('A')
            shifted = (ord(char) - ord('A') + shift) % 26
            plaintext += chr(shifted + ord('A'))
            keyIndex += 1
        else:
            plaintext += char
    return plaintext

def vingenere_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_length = len(key)
    ciphertext = ciphertext.upper()
    keyIndex = 0 #this is here because using i to determine shift
    #gets messed up because of the existence of many spaces
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[keyIndex % key_length]) - ord('A')
            shifted = (ord(char) - ord('A') - shift) % 26
            plaintext += chr(shifted + ord('A'))
            keyIndex += 1
        else:
            plaintext += char
    return plaintext


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
while not (menuOption.isdigit() and within_range(int(menuOption), 1, 3)):
    menuOption = input(menuOption + " is not a valid input, please enter a value from 1 - 3 ")
print("\nok you said " + menuOption)
if menuOption == "1":
    #Decrypt given a key
    ciphertext = input("Enter ciphertext ")
    key = input("Enter key ")
    plaintext = vingenere_decrypt(ciphertext, key)
    print(f"Ciphertext: {ciphertext}\n")
    print(f"Key: {key}\n")
    print(f"Plaintext: {plaintext}\n")
elif menuOption == "2":
    #Decrypt, but need to find key
    ciphertext = input("Enter ciphertext: ")
    print(f"Ciphertext: {ciphertext}\n")
    print(f"Key: {key}\n")
    print(f"Plaintext: {plaintext}\n")
elif menuOption == "3":
    #Encrypt given a key
    plaintext = input("Enter plaintext ")
    key = input("Enter key ")
    ciphertext = vingenere_encrypt(plaintext, key)
    print(f"Plaintext: {plaintext}\n")
    print(f"Key: {key}\n")
    print(f"Ciphertext: {ciphertext}\n")



