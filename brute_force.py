# Brute Force RSA Attack
# crypto_lab_Charis

from rsa import generate_keypair, encrypt, decrypt

def brute_force_attack(public_key, encrypted_message):
    e, n = public_key
    
    # Δοκιμάζουμε όλους τους πιθανούς παράγοντες του n
    for i in range(2, n):
        if n % i == 0:
            p = i
            q = n // i
            break
    
    print(f"Βρέθηκαν οι παράγοντες: p={p}, q={q}")
    
    # Ανακατασκευή ιδιωτικού κλειδιού
    _, private_key = generate_keypair(p, q)
    
    # Αποκρυπτογράφηση
    decrypted = decrypt(private_key, encrypted_message)
    return decrypted

if __name__ == "__main__":
    p, q = 61, 53
    public_key, _ = generate_keypair(p, q)
    
    message = "HI"
    encrypted = encrypt(public_key, message)
    print("Κρυπτογραφημένο:", encrypted)
    
    cracked = brute_force_attack(public_key, encrypted)
    print("Αποκρυπτογραφημένο (brute force):", cracked)
