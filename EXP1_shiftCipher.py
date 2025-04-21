def encrypt(text, s): 
    result = "" 
    # Traverse the text 
    for i in range(len(text)): 
        char = text[i] 
        # Encrypt uppercase characters 
        if char.isupper(): 
            result += chr((ord(char) + s - 65) % 26 + 65) 
        # Encrypt lowercase characters 
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char  # Leave non-alphabet characters unchanged
    return result 

def decrypt(text, s): 
    result = "" 
    # Traverse the text
    for j in range(len(text)): 
        char = text[j]       
        if char.isupper(): 
            result += chr((ord(char) - s - 65) % 26 + 65) 
        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)
        else:
            result += char  # Leave non-alphabet characters unchanged
    return result 

# Encryption part
text = input("Enter plain text: ") 
s = int(input("Enter key value: ")) 
print("Text       :", text) 
print("Shift      :", s) 
cipher = encrypt(text, s)
print("Cipher     :", cipher)

# Decryption part
text = input("\nEnter cipher text: ") 
s = int(input("Enter key value: ")) 
print("CipherText :", text) 
print("Shift      :", s) 
plain = decrypt(text, s)
print("Plain Text :", plain)
