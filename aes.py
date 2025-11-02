# aes_fernet_example.py
# Simple AES-like example using cryptography.Fernet
# Run: python aes_fernet_example.py
# Install dependency if needed:
# pip install cryptography

def try_aes_demo():
    try:
        from cryptography.fernet import Fernet
    except Exception:
        print("cryptography library is not installed. Install with:\n  pip install cryptography")
        return

    # Generate a key (in real project store it safely)
    key = Fernet.generate_key()
    f = Fernet(key)

    plaintext = b"HELLO WORLD"
    token = f.encrypt(plaintext)
    print("Key (base64):", key.decode())
    print("Encrypted (token):", token)
    # Decrypt
    orig = f.decrypt(token)
    print("Decrypted:", orig.decode())

if __name__ == "__main__":
    try_aes_demo()