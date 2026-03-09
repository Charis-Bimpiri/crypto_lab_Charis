def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y
def mod_inverse(a, n):
    gcd, x, _ = extended_gcd(a, n)
    if gcd != 1:
        raise ValueError(f"Το inverse του {a} mod {n} δεν υπάρχει!")
    return x % n
def power_mod(base, exp, mod):
    return pow(base, exp, mod)
