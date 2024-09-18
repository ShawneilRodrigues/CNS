# Function to encrypt using Rail Fence Cipher
def rail_fence_encrypt(plaintext, key):
    # Create the fence (matrix)
    fence = [['' for _ in range(len(plaintext))] for _ in range(key)]
    row, direction = 0, 1

    # Place the characters in the zig-zag pattern
    for i, char in enumerate(plaintext):
        fence[row][i] = char
        row += direction
        
        # Reverse direction if we hit the top or bottom
        if row == 0 or row == key - 1:
            direction = -direction

    # Read the characters row by row to get the ciphertext
    ciphertext = ''.join(''.join(row) for row in fence)
    return ciphertext

# Function to decrypt using Rail Fence Cipher
def rail_fence_decrypt(ciphertext, key):
    # Create the fence (matrix)
    fence = [['' for _ in range(len(ciphertext))] for _ in range(key)]
    row, direction = 0, 1

    # Mark the positions in the fence where the characters will go
    for i in range(len(ciphertext)):
        fence[row][i] = '*'
        row += direction
        
        # Reverse direction if we hit the top or bottom
        if row == 0 or row == key - 1:
            direction = -direction

    # Fill the fence with the ciphertext
    index = 0
    for r in range(key):
        for c in range(len(ciphertext)):
            if fence[r][c] == '*' and index < len(ciphertext):
                fence[r][c] = ciphertext[index]
                index += 1

    # Read the characters in the zig-zag pattern to get the plaintext
    plaintext = []
    row, direction = 0, 1
    for i in range(len(ciphertext)):
        plaintext.append(fence[row][i])
        row += direction
        if row == 0 or row == key - 1:
            direction = -direction

    return ''.join(plaintext)

# Example usage
if __name__ == "__main__":
    plaintext = "defendtheeastwall"
    key = 3
    
    encrypted_text = rail_fence_encrypt(plaintext, key)
    print(f"Encrypted: {encrypted_text}")
    
    decrypted_text = rail_fence_decrypt(encrypted_text, key)
    print(f"Decrypted: {decrypted_text}")
