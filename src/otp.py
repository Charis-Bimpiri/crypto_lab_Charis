import random
import string

def generate_key(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

def encrypt(message, key):
    result = ""
    key_index = 0
    for char in message:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def decrypt(message, key):
    result = ""
    key_index = 0
    for char in message:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

message = "HELLO"
key = generate_key(len(message))
print("Message: ", message)
print("Key:     ", key)
encrypted = encrypt(message, key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypt(encrypted, key))
