import math

def encrypt_columnar_cipher(plaintext, key):
    # Remove spaces from the key and sort the key to get the column order
    key_order = sorted(list(key))
    key_indices = [key.index(k) for k in key_order]

    # Remove spaces from the plaintext
    plaintext = plaintext.replace(" ", "")
    
    # Calculate number of rows needed for the grid
    num_columns = len(key)
    num_rows = math.ceil(len(plaintext) / num_columns)

    # Fill the grid with characters row by row
    grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]
    
    index = 0
    for r in range(num_rows):
        for c in range(num_columns):
            if index < len(plaintext):
                grid[r][c] = plaintext[index]
                index += 1

    # Read the columns in the order defined by the key
    ciphertext = ''
    for k in key_indices:
        for r in range(num_rows):
            if grid[r][k]:
                ciphertext += grid[r][k]

    return ciphertext

def decrypt_columnar_cipher(ciphertext, key):
    # Sort the key to get the column order
    key_order = sorted(list(key))
    key_indices = [key.index(k) for k in key_order]

    # Calculate the number of rows and columns
    num_columns = len(key)
    num_rows = math.ceil(len(ciphertext) / num_columns)

    # Fill the columns with characters from the ciphertext
    grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]
    index = 0
    for k in key_indices:
        for r in range(num_rows):
            if index < len(ciphertext):
                grid[r][k] = ciphertext[index]
                index += 1

    # Read the grid row by row to retrieve the original message
    plaintext = ''
    for r in range(num_rows):
        for c in range(num_columns):
            if grid[r][c]:
                plaintext += grid[r][c]

    return plaintext


# Example usage
plaintext = "HELLO WORLD"
key = "31452"

ciphertext = encrypt_columnar_cipher(plaintext, key)
print(f"Ciphertext: {ciphertext}")

decrypted_message = decrypt_columnar_cipher(ciphertext, key)
print(f"Decrypted message: {decrypted_message}")
