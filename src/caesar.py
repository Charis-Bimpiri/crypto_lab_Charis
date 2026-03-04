def encrypt(message, key):
    result = ""
    for char in message:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(message, key):
    return encrypt(message, -key)

def brute_force(message):
    print("--- Brute Force Attack ---")
    for key in range(1, 26):
        attempt = decrypt(message, key)
        print(f"Key {key:2}: {attempt}")
encrypted = encrypt("HELLO", 3)
print("Encrypted:", encrypted)
brute_force(encrypted)
