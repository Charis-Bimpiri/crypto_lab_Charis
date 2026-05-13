# Comparison: RSA vs Brute Force

## RSA Security

RSA is secure when p and q are large primes (1024+ bits).
Factoring n becomes computationally infeasible.

## Brute Force Attack

With small primes like p=61, q=53:
- n = 3233
- We simply try all numbers from 2 to n
- We find p and q quickly
- We reconstruct the private key
- Game over

## Why it fails with large keys

If n has 2048 bits, brute force would take longer than
the age of the universe.
