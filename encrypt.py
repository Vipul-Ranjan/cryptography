# Caesar Cipher in Python (with clear entry point)

def caesar_encrypt(text, shift):
    """Encrypts the text using Caesar Cipher with the given shift."""
    result = ""
    for char in text:
        if char.isalpha():  # Only shift letters
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char  # Keep spaces, numbers, and symbols unchanged
    return result


def caesar_decrypt(text, shift):
    """Decrypts the text using Caesar Cipher with the given shift."""
    return caesar_encrypt(text, -shift)  # Shift backwards for decryption


# --- Program starts here ---
if __name__ == "__main__":
    plaintext = input("Enter the text: ")           # Get message from user
    shift = int(input("Enter the shift key: "))     # Get shift value (number)

    encrypted = caesar_encrypt(plaintext, shift)   # Encrypt
    decrypted = caesar_decrypt(encrypted, shift)   # Decrypt

    print("\nPlaintext: ", plaintext)
    print("Encrypted: ", encrypted)
    print("Decrypted: ", decrypted)
