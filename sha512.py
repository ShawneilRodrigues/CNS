import hashlib

def sha512_hash(data):
    # Create a new sha512 hash object
    sha512 = hashlib.sha512()

    # Update the hash object with the bytes-like object
    sha512.update(data.encode('utf-8'))

    # Return the hexadecimal representation of the digest
    return sha512.hexdigest()

# Example usage
input_string = "Hello, world!"
hashed_output = sha512_hash(input_string)
print(f"SHA-512 Hash of '{input_string}': {hashed_output}")
