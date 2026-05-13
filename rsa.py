# RSA Implementation from scratch
# crypto_lab_Charis

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y
def mod_inverse(e, phi):
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise Exception("Δεν υπάρχει αντίστροφο!")
    return x % phi
def power_mod(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = result * base % mod
        exp = exp // 2
        base = base * base % mod
    return result
def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1
    
    d = mod_inverse(e, phi)
    
    return (e, n), (d, n)
def encrypt(public_key, message):
    e, n = public_key
    return [power_mod(ord(char), e, n) for char in message]

def decrypt(private_key, encrypted):
    d, n = private_key
    return ''.join([chr(power_mod(char, d, n)) for char in encrypted])
if __name__ == "__main__":
    p = 61
    q = 53
    public_key, private_key = generate_keypair(p, q)
    print("Δημόσιο κλειδί:", public_key)
    print("Ιδιωτικό κλειδί:", private_key)
    
    message = "HELLO"
    encrypted = encrypt(public_key, message)
    decrypted = decrypt(private_key, encrypted)
    print("Αρχικό μήνυμα:", message)
    print("Κρυπτογραφημένο:", encrypted)
    print("Αποκρυπτογραφημένο:", decrypted)
