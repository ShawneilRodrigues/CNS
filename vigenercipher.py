# Function to encrypt using Vigenère Cipher
def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = []
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            # Get shift amount from the key
            shift = ord(key[key_index]) - ord('A')
            # Encrypt character and append to result
            encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            ciphertext.append(encrypted_char)
            # Move to the next letter in the key
            key_index = (key_index + 1) % len(key)
        else:
            # Non-alphabet characters are not encrypted
            ciphertext.append(char)
    
    return ''.join(ciphertext)

# Function to decrypt using Vigenère Cipher
def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = []
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            # Get shift amount from the key
            shift = ord(key[key_index]) - ord('A')
            # Decrypt character and append to result
            decrypted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
            plaintext.append(decrypted_char)
            # Move to the next letter in the key
            key_index = (key_index + 1) % len(key)
        else:
            # Non-alphabet characters are not decrypted
            plaintext.append(char)
    
    return ''.join(plaintext)

# Example usage
if __name__ == "__main__":
    plaintext = "ATTACK AT DAWN"
    key = "LEMON"
    
    encrypted_text = vigenere_encrypt(plaintext, key)
    print(f"Encrypted: {encrypted_text}")
    
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print(f"Decrypted: {decrypted_text}")
