from src.math_utils import gcd, mod_inverse, power_mod
def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 2
    while gcd(e, phi) != 1:
        e += 1
    
    d = mod_inverse(e, phi)
    
    return (e, n), (d, n)
def encrypt(message, public_key):
    e, n = public_key
    return power_mod(message, e, n)

def decrypt(ciphertext, private_key):
    d, n = private_key
    return power_mod(ciphertext, d, n)
