Algorithm Comparison
A comparison of the cryptographic algorithms implemented in this project, evaluated across key dimensions of security, practicality, and mathematical complexity.
Comparison Table
Algorithm	Type	Key Space	Security Level	Key Distribution	Mathematical Basis
Caesar	Symmetric	25 keys	Very weak	Shared secret	Modular arithmetic (mod 26)
Vigenère	Symmetric	26ⁿ (n = key length)	Weak	Shared secret	Modular arithmetic (mod 26)
One-Time Pad	Symmetric	2ⁿ (n = message length)	Perfect (in theory)	Shared secret	XOR / modular arithmetic
RSA	Asymmetric	2²⁰⁴⁸ (for 2048-bit keys)	Strong	Public key infrastructure	Number theory (factorization)
Security Analysis
Caesar Cipher
The Caesar cipher has only 25 possible keys, making it trivially broken by brute-force. Even without a computer, an attacker can try all shifts in minutes. It provides no meaningful security by modern standards.
Vigenère Cipher
The Vigenère cipher improves on Caesar by using a keyword, expanding the key space to 26ⁿ. However, it is vulnerable to the index of coincidence attack: if the key length can be determined (e.g. via the Kasiski test), the cipher reduces to multiple Caesar ciphers and can be broken with frequency analysis.
One-Time Pad
The One-Time Pad is the only cipher with proven perfect secrecy, as demonstrated by Claude Shannon in 1949. If the key is truly random, used only once, and kept secret, it is mathematically impossible to break. In practice, however, securely distributing a key as long as the message is a significant logistical challenge.
RSA
RSA is an asymmetric cipher: encryption and decryption use different keys. Its security rests on the hardness of the integer factorization problem — given n = p · q, recovering p and q is computationally infeasible for large n. Unlike the classical ciphers above, RSA does not require a pre-shared secret, making it suitable for secure communication over public channels.
Key Distribution Problem
One of the fundamental challenges in cryptography is how two parties can share a secret key over an insecure channel. Classical symmetric ciphers (Caesar, Vigenère, OTP) all require a pre-shared key, which creates a chicken-and-egg problem: you need a secure channel to share the key, but you need the key to have a secure channel.
RSA solves this elegantly through public-key cryptography: the public key can be shared openly, while the private key never leaves its owner. Anyone can encrypt a message using the public key, but only the holder of the private key can decrypt it.
Computational Complexity
Algorithm	Encryption	Decryption	Attack (brute-force)
Caesar	O(n)	O(n)	O(1) — 25 keys
Vigenère	O(n)	O(n)	O(26ᵏ) — k = key length
One-Time Pad	O(n)	O(n)	Impossible in theory
RSA	O(log² e · log n)	O(log² d · log n)	O(√n) — trial division
Conclusion
The progression from Caesar to RSA reflects the evolution of cryptographic thinking: from simple substitution to mathematically grounded systems whose security can be formally reasoned about. The classical ciphers are historically significant and pedagogically useful, but only RSA (and modern systems built on similar principles) provides security suitable for real-world applications.
