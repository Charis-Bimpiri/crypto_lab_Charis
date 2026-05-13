# Trace Example

A step-by-step example of RSA with p=61, q=53.

## Key Generation

- n = 61 * 53 = 3233
- phi = 60 * 52 = 3120
- e = 7 (coprime to 3120)
- d = 2753 (since 7 * 2753 ≡ 1 mod 3120)

Public key: (7, 3233)
Private key: (2753, 3233)

## Encrypting the letter "H"

- ASCII value of H = 72
- c = 72^7 mod 3233 = 1087

## Decrypting

- m = 1087^2753 mod 3233 = 72
- chr(72) = "H"

It works because of Euler's theorem:
m^(e*d) ≡ m (mod n)
