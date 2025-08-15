def encr(text,shift):
    result =""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result = result + chr((ord(char)-65+shift)%26 + 65)
            else:
                result= result + chr((ord(char)-97 + shift)% 26 +97)
        else:
            result = result+char
    return result
if __name__ == "__main__":
    plaintext = input("Plaintext: ")
    shift = int(input("Shift: "))
    encrypted = encr(plaintext, shift)
    print("\nPlaintext: ", plaintext)
    print("Encrypted: ", encrypted)
