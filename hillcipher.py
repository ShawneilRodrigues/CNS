import numpy as np

# Helper functions
def mod_inverse(a, m):
    # Function to find the modular inverse of a under modulo m
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_mod_inverse(matrix, modulus):
    # Calculate the modular inverse of the matrix
    det = int(np.round(np.linalg.det(matrix)))  # Determinant of the matrix
    det_inv = mod_inverse(det, modulus)  # Modular inverse of the determinant
    if det_inv is None:
        raise ValueError("Matrix is not invertible under mod {}".format(modulus))
    
    # Calculate the adjugate matrix and multiply by the modular inverse of the determinant
    matrix_mod_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )
    return matrix_mod_inv % modulus

# Hill Cipher encryption function
def encrypt(message, key_matrix):
    message = message.replace(" ", "").upper()
    modulus = 26
    key_size = key_matrix.shape[0]
    
    # Ensure message length is a multiple of key size
    while len(message) % key_size != 0:
        message += 'X'  # Padding with 'X'
    
    # Convert message to numerical form
    message_vector = [ord(char) - ord('A') for char in message]
    message_matrix = np.array(message_vector).reshape(-1, key_size)
    
    # Encrypt by multiplying the message matrix by the key matrix
    encrypted_matrix = (message_matrix @ key_matrix) % modulus
    
    # Convert back to letters
    encrypted_message = ''.join([chr(int(num) + ord('A')) for row in encrypted_matrix for num in row])
    return encrypted_message

# Hill Cipher decryption function
def decrypt(encrypted_message, key_matrix):
    modulus = 26
    key_size = key_matrix.shape[0]
    
    # Convert encrypted message to numerical form
    encrypted_vector = [ord(char) - ord('A') for char in encrypted_message]
    encrypted_matrix = np.array(encrypted_vector).reshape(-1, key_size)
    
    # Find the modular inverse of the key matrix
    key_matrix_inv = matrix_mod_inverse(key_matrix, modulus)
    
    # Decrypt by multiplying the encrypted matrix by the inverse key matrix
    decrypted_matrix = (encrypted_matrix @ key_matrix_inv) % modulus
    
    # Convert back to letters
    decrypted_message = ''.join([chr(int(num) + ord('A')) for row in decrypted_matrix for num in row])
    return decrypted_message

# Example usage
if __name__ == "__main__":
    # Example 2x2 key matrix
    key_matrix = np.array([[6, 24], [1, 13]])
    
    message = "HELLO"
    encrypted_message = encrypt(message, key_matrix)
    print("Encrypted message:", encrypted_message)
    
    decrypted_message = decrypt(encrypted_message, key_matrix)
    print("Decrypted message:", decrypted_message)
