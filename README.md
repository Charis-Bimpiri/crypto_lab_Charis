# crypto_lab_Charis

This project is part of my portfolio as a mathematics graduate
exploring cryptography and cybersecurity.

I implemented RSA from scratch in Python without using any 
cryptographic libraries. The math behind it comes from Number 
Theory - modular arithmetic and the Euclidean algorithm.

## Files

- `rsa.py` - key generation, encryption, decryption
- `brute_force.py` - shows why small RSA keys are unsafe

## How RSA works (briefly)

Pick two primes p and q. Compute n = p*q and phi = (p-1)*(q-1).
Find e coprime to phi (public key) and d its modular inverse 
(private key). Encrypt with e, decrypt with d.

## Note

I used small primes (p=61, q=53) to keep it readable.
Real RSA uses primes with hundreds of digits.
