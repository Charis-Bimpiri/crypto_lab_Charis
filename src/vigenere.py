def encrypt(message, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in message:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def decrypt(message, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in message:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

encrypted = encrypt("HELLO", "KEY")
print("Encrypted:", encrypted)
print("Decrypted:", decrypt(encrypted, "KEY"))
