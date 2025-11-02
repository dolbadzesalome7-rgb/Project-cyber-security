# caesar_cipher.py
# Simple Caesar cipher example with Georgian comments
# Run: python caesar_cipher.py

def caesar_encrypt(text: str, shift: int) -> str:
    result = ""
    for ch in text:
        if ch.isalpha():
            start = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - start + shift) % 26 + start)
        else:
            result += ch
    return result

def caesar_decrypt(text: str, shift: int) -> str:
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    # მაგალითი — შეგიძლია შეცვალო ტექსტი და shift
    plaintext = "HELLO WORLD"
    shift = 3

    print("Plaintext:", plaintext)
    encrypted = caesar_encrypt(plaintext, shift)
    print("Encrypted (shift=3):", encrypted)   # KHOOR ZRUOG
    decrypted = caesar_decrypt(encrypted, shift)
    print("Decrypted:", decrypted)