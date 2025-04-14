def generate_matrix(key):
    key = key.upper().replace("J", "I")
    seen = set()
    matrix = []

    for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen and char.isalpha():
            seen.add(char)
            matrix.append(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]


def format_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    formatted = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i + 1 < len(text) else 'X'
        if a == b:
            formatted += a + 'X'
            i += 1
        else:
            formatted += a + b
            i += 2
    if len(formatted) % 2 != 0:
        formatted += 'X'
    return formatted


def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None


def playfair_cipher(text, key, mode):
    matrix = generate_matrix(key)
    text = format_text(text)
    result = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            if mode == "encrypt":
                result += matrix[row1][(col1 + 1) % 5]
                result += matrix[row2][(col2 + 1) % 5]
            elif mode == "decrypt":
                result += matrix[row1][(col1 - 1) % 5]
                result += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            if mode == "encrypt":
                result += matrix[(row1 + 1) % 5][col1]
                result += matrix[(row2 + 1) % 5][col2]
            elif mode == "decrypt":
                result += matrix[(row1 - 1) % 5][col1]
                result += matrix[(row2 - 1) % 5][col2]
        else:
            result += matrix[row1][col2]
            result += matrix[row2][col1]

    return result


# Encryption
plaintext = input("Enter plaintext to encrypt (only letters): ")
key = input("Enter key (only letters, no spaces): ")

ciphertext = playfair_cipher(plaintext, key, "encrypt")
print("Ciphertext:", ciphertext)

# Decryption
ciphertext_to_decrypt = input("Enter ciphertext to decrypt (only letters): ")
key_for_decryption = input("Enter key for decryption (only letters, no spaces): ")

decrypted_text = playfair_cipher(ciphertext_to_decrypt, key_for_decryption, "decrypt")
print("Decrypted Text:", decrypted_text)
