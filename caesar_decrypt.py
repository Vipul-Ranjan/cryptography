def decr(text , shift):
    result=""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result = result +  chr((ord(char)- 65 - shift) % 26 + 65)
            else:
                result = result + chr((ord(char) - 97 - shift) % 26 + 97)
    return result

if __name__ =='__main__':
    plaintext = input("enter the text you wanrt to decrypt\n")
    shift = int(input("enter the key shift\n"))
    result = decr(plaintext,shift)
    print("decrypted result is",result )
