def vernam_cipher(plaintext, key, mode):
    if len(plaintext) != len(key):
        print("Error: Key must be the same length as plaintext.")
        return None

    result = ""
    for i in range(len(plaintext)):
        plaintext_value = ord(plaintext[i].upper()) - ord('A')
        key_value = ord(key[i].upper()) - ord('A')

        if mode == 'encrypt':
            cipher_value = (plaintext_value + key_value) % 26
        elif mode == 'decrypt':
            cipher_value = (plaintext_value - key_value) % 26
        else:
            print("Invalid mode. Choose 'encrypt' or 'decrypt'.")
            return None

        result += chr(cipher_value + ord('A'))

    return result


plaintext = input("Enter plaintext to encrypt (only letters, no spaces): ")
key = input("Enter key (must be same length as plaintext, only letters): ")

ciphertext = vernam_cipher(plaintext, key, 'encrypt')
if ciphertext:
    print("Ciphertext:", ciphertext)

ciphertext_to_decrypt = input("Enter ciphertext to decrypt (only letters, no spaces): ")
key_for_decryption = input("Enter key for decryption (must be same length as ciphertext, only letters): ")

decrypted_text = vernam_cipher(ciphertext_to_decrypt, key_for_decryption, 'decrypt')
if decrypted_text:
    print("Decrypted Text:", decrypted_text)
