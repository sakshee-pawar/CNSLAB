def encrypt(plain_text, key):
    cipher_text = ""	
    for char in plain_text:
        if char.isalpha():
            char = char.upper()
            encrypted_char = chr(((ord(char) - ord('A')) * key) % 26 + ord('A'))
            cipher_text += encrypted_char
        else:
            cipher_text += char
    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ""
    try:
        key_inverse = pow(key, -1, 26)  # Modular inverse of key under mod 26
    except ValueError:
        return "Key has no modular inverse under mod 26. Decryption not possible."

    for char in cipher_text:
        if char.isalpha():
            char = char.upper()
            decrypted_char = chr(((ord(char) - ord('A')) * key_inverse) % 26 + ord('A'))
            plain_text += decrypted_char
        else:
            plain_text += char
    return plain_text

# Input from user
plain_text = input("Enter the plain text: ")

# Input key with validation
while True:
    try:
        key = int(input("Enter the key (an integer): "))
        if key < 1 or key >= 26:
            raise ValueError("Key must be between 1 and 25.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid integer for the key.")

# Encrypt and Decrypt
cipher_text = encrypt(plain_text, key)
print("Encrypted:", cipher_text)

decrypted_text = decrypt(cipher_text, key)
print("Decrypted:", decrypted_text)
