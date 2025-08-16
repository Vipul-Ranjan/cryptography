import learning
import learning2






if __name__ == '__main__':
        plaintext = input("enter the text you want to encrypt or decrypt\n")
        shift = int(input("enter the key shift\n"))
        encrypted_text = learning.encr(plaintext,shift)
        print("encryted value of the given text is",learning.encr(plaintext,shift))
        print("decryption of the above text is",learning2.decr(encrypted_text,shift))
