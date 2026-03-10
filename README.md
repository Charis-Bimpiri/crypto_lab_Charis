# crypto_lab

A cryptography portfolio project that implements both classical and contemporary encryption algorithms, built from their mathematical foundations, created as a component of an application to a graduate cybersecurity program.

## Overview

This project showcases a comprehensive, from-scratch development of cryptographic systems, beginning with the foundational mathematics and advancing to full implementations of encryption and attack methods. Every algorithm is built independently, without using external cryptographic libraries, aiming to clarify the mathematical concepts that form the basis of contemporary security frameworks.

## Project Structure

```
crypto_lab/
├── src/
│   ├── math_utils.py     # Core cryptographic mathematics
│   ├── caesar.py         # Caesar cipher + brute-force attack
│   ├── vigenere.py       # Vigenère cipher
│   ├── otp.py            # One-Time Pad
│   └── rsa.py            # RSA encryption system
├── attacks/
│   └── rsa_attack.py     # Brute-force factorization attack on RSA
├── docs/
│   ├── comparison.md     # Algorithm security comparison
│   └── trace_example.md  # Step-by-step mathematical trace
└── tests/
```

## Mathematical Foundations

Before implementing any modern cipher, this project establishes the necessary mathematical infrastructure in `src/math_utils.py`:

- **Greatest Common Divisor (GCD)** — Euclidean algorithm in O(log n) time
- **Extended Euclidean Algorithm** — computes Bézout coefficients for solving linear Diophantine equations
- **Modular Inverse** — derived from the Extended Euclidean Algorithm; exists if and only if gcd(a, n) = 1
- **Modular Exponentiation** — fast computation of aᵏ mod n, essential for RSA performance

These primitives reflect a deliberate choice to understand cryptography at the level of number theory rather than treating it as a black box.

## Implementations

### Classical Ciphers

| Algorithm | Key Space | Security |
|-----------|-----------|----------|
| Caesar | 25 possible keys | Trivially broken by brute-force |
| Vigenère | 26ⁿ (n = key length) | Vulnerable to index of coincidence analysis |
| One-Time Pad | 2ⁿ (n = message length) | Theoretically unbreakable if key is truly random |

### RSA

RSA is implemented across two stages: key generation and encryption/decryption.

**Key Generation:**
1. Select two prime numbers p and q
2. Compute n = p · q (public modulus)
3. Compute φ(n) = (p−1)(q−1) (Euler's totient)
4. Select e such that gcd(e, φ(n)) = 1 (public exponent)
5. Compute d = e⁻¹ mod φ(n) using the Extended Euclidean Algorithm (private exponent)

**Encryption:** c = mᵉ mod n

**Decryption:** m = cᵈ mod n

Correctness follows from Euler's theorem: since e·d ≡ 1 (mod φ(n)), we have mᵉᵈ ≡ m (mod n).

### Brute-Force Attack on RSA

The attack in `attacks/rsa_attack.py` demonstrates why small RSA keys are insecure. Given only the public key (e, n), the attack:

1. Factorizes n by trial division up to √n
2. Recovers φ(n) = (p−1)(q−1)
3. Computes the private key d = e⁻¹ mod φ(n)

This is computationally feasible for small n, but infeasible for 2048-bit keys, where √n contains approximately 300 digits. The security of RSA rests entirely on the hardness of integer factorization.

## Setup

```bash
git clone https://github.com/Charis-Bimpiri/crypto_lab.git
cd crypto_lab
python3 -m venv venv
source venv/bin/activate
```

## Usage

```python
from src.rsa import generate_keypair, encrypt_text, decrypt_text

public_key, private_key = generate_keypair(61, 53)
ciphertext = encrypt_text("hello", public_key)
plaintext  = decrypt_text(ciphertext, private_key)
```

## Motivation
This project was built to close the gap between theoretical 
mathematics and real-world cybersecurity. The focus is on 
clarity and mathematical correctness rather than performance, 
with the goal of understanding why these systems are secure, 
not just how to use them.
