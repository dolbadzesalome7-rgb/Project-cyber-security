# xor_cipher.py
# Simple XOR cipher demo (numeric key)
# Run: python xor_cipher.py

def xor_encrypt_decrypt(text: str, key: int) -> str:
    """Encrypts/decrypts text with a numeric key 0..255"""
    out = []
    for ch in text:
        out.append(chr(ord(ch) ^ key))
    return "".join(out)

if __name__ == "__main__":
    plaintext = "HELLO WORLD"
    key = 123  # small numeric key for demo

    print("Plaintext:", plaintext)
    cipher = xor_encrypt_decrypt(plaintext, key)
    print("Encrypted (XOR):", cipher)          # გაძლიერებული/უცნაური სიმბოლოები
    recovered = xor_encrypt_decrypt(cipher, key)
    print("Decrypted:", recovered)