import math

def transposition_cipher(message, key, mode='encrypt'):
    # Remove spaces for encryption
    if mode == 'encrypt':
        message = message.replace(" ", "")
    
    # Encryption
    if mode == 'encrypt':
        cipher_text = [''] * key
        
        # Loop through each column
        for column in range(key):
            current_index = column
            while current_index < len(message):
                cipher_text[column] += message[current_index]
                current_index += key
        
        return ''.join(cipher_text)
    
    # Decryption
    elif mode == 'decrypt':
        num_columns = key
        num_rows = math.ceil(len(message) / key)
        num_shaded_boxes = (num_columns * num_rows) - len(message)
        
        plain_text = [''] * num_rows
        column, row = 0, 0
        
        for symbol in message:
            plain_text[row] += symbol
            row += 1
            
            if (row == num_rows) or (row == num_rows - 1 and column >= num_columns - num_shaded_boxes):
                row = 0
                column += 1
        
        return ''.join(plain_text)

# Example usage
message = "This is a secret message"
key = 5

# Encrypt the message
encrypted = transposition_cipher(message, key, mode='encrypt')
print(f"Encrypted message: {encrypted}")

# Decrypt the message
decrypted = transposition_cipher(encrypted, key, mode='decrypt')
print(f"Decrypted message: {decrypted}")
