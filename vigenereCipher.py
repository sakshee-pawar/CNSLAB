def vigenere_cipher(text, key, mode):
    text = text.upper()
    key = key.upper()
    key_repeated = "".join(key[i % len(key)] for i in range(len(text)))
    result = ""

    for i in range(len(text)):
        text_val = ord(text[i]) - ord('A')
        key_val = ord(key_repeated[i]) - ord('A')

        if mode == 'encrypt':
            new_val = (text_val + key_val) % 26  # Encryption formula
        elif mode == 'decrypt':
            new_val = (text_val - key_val) % 26  # Decryption formula
        else:
            print("Invalid mode. Choose 'encrypt' or 'decrypt'.")
            return None

        result += chr(new_val + ord('A'))

    return result


# Encryption
plaintext = input("Enter plaintext to encrypt (only letters, no spaces): ")
key = input("Enter key (only letters, no spaces): ")

ciphertext = vigenere_cipher(plaintext, key, 'encrypt')
if ciphertext:
    print("Ciphertext:", ciphertext)

# Decryption
ciphertext_to_decrypt = input("Enter ciphertext to decrypt (only letters, no spaces): ")
key_for_decryption = input("Enter key for decryption (only letters, no spaces): ")

decrypted_text = vigenere_cipher(ciphertext_to_decrypt, key_for_decryption, 'decrypt')
if decrypted_text:
    print("Decrypted Text:", decrypted_text)
