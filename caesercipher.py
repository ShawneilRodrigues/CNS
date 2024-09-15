def caesar_cipher(text, shift):
    result = ""

    # Traverse each character in the text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        # If it's not an alphabet, don't change it
        else:
            result += char

    return result

def caesar_decrypt(cipher_text, shift):
    result = ""

    # Traverse each character in the text
    for i in range(len(cipher_text)):
        char = cipher_text[i]

        # Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)

        # Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)

        # If it's not an alphabet, don't change it
        else:
            result += char

    return result

# Example usage
text = "Hello, World!"
shift = 3

# Encrypt the text
encrypted_text = caesar_cipher(text, shift)
print("Encrypted Text: ", encrypted_text)

# Decrypt the text
decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Decrypted Text: ", decrypted_text)
