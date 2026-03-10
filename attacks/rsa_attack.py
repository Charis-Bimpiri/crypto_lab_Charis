from math import isqrt
from src.math_utils import mod_inverse

def factorize(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return i, n // i
    return None

def brute_force_rsa(e, n):
    p, q = factorize(n)
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    return d
