import caesar_encrypt
import caesar_decrypt







if __name__ == '__main__':
        plaintext = input("enter the text you want to encrypt or decrypt\n")
        shift = int(input("enter the key shift\n"))
        encrypted_text = caesar_encrypt.encr(plaintext,shift)
        print("encryted value of the given text is",caesar_encrypt.encr(plaintext,shift))
        print("decryption of the above text is",caesar_decrypt.decr(encrypted_text,shift))
