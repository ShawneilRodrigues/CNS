import string

# Function to generate the 5x5 key matrix
def generate_key_matrix(key):
    key = key.lower().replace('j', 'i')
    key_matrix = []
    key_set = set()
    for char in key:
        if char not in key_set and char in string.ascii_lowercase:
            key_matrix.append(char)
            key_set.add(char)
    
    for char in string.ascii_lowercase.replace('j', ''):
        if char not in key_set:
            key_matrix.append(char)
            key_set.add(char)
    
    return [key_matrix[i:i+5] for i in range(0, 25, 5)]

# Function to prepare text for encryption or decryption
def prepare_text(text, encrypt=True):
    text = text.lower().replace('j', 'i').replace(" ", "")
    prepared_text = ""
    i = 0
    while i < len(text):
        prepared_text += text[i]
        if i+1 < len(text) and text[i] == text[i+1]:
            prepared_text += 'x'
        elif i+1 < len(text):
            prepared_text += text[i+1]
            i += 1
        i += 1
    
    if len(prepared_text) % 2 != 0:
        prepared_text += 'x'
    return prepared_text

# Function to get position of a character in the key matrix
def get_position(key_matrix, char):
    for i, row in enumerate(key_matrix):
        if char in row:
            return i, row.index(char)
    return None

# Function to encrypt/decrypt a pair of characters
def process_pair(key_matrix, char1, char2, encrypt=True):
    row1, col1 = get_position(key_matrix, char1)
    row2, col2 = get_position(key_matrix, char2)

    if row1 == row2:
        if encrypt:
            return key_matrix[row1][(col1+1)%5] + key_matrix[row2][(col2+1)%5]
        else:
            return key_matrix[row1][(col1-1)%5] + key_matrix[row2][(col2-1)%5]
    elif col1 == col2:
        if encrypt:
            return key_matrix[(row1+1)%5][col1] + key_matrix[(row2+1)%5][col2]
        else:
            return key_matrix[(row1-1)%5][col1] + key_matrix[(row2-1)%5][col2]
    else:
        return key_matrix[row1][col2] + key_matrix[row2][col1]

# Function to encrypt the text using Playfair cipher
def playfair_encrypt(plaintext, key):
    key_matrix = generate_key_matrix(key)
    prepared_text = prepare_text(plaintext)
    ciphertext = ""
    for i in range(0, len(prepared_text), 2):
        ciphertext += process_pair(key_matrix, prepared_text[i], prepared_text[i+1], encrypt=True)
    return ciphertext.upper()

# Function to decrypt the text using Playfair cipher
def playfair_decrypt(ciphertext, key):
    key_matrix = generate_key_matrix(key)
    ciphertext = ciphertext.lower().replace(" ", "")
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        plaintext += process_pair(key_matrix, ciphertext[i], ciphertext[i+1], encrypt=False)
    return plaintext

# Example usage
if __name__ == "__main__":
    key = "playfairexample"
    plaintext = "Hide the gold in the tree stump"
    
    encrypted_text = playfair_encrypt(plaintext, key)
    print(f"Encrypted: {encrypted_text}")
    
    decrypted_text = playfair_decrypt(encrypted_text, key)
    print(f"Decrypted: {decrypted_text}")
