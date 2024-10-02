import struct

def left_rotate(n, b):
    """Perform left bit rotation on a 32-bit integer n by b bits."""
    return ((n << b) | (n >> (32 - b))) & 0xffffffff

def sha1(data):
    # Initialize variables for SHA-1
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Preprocessing: Padding the message
    original_byte_len = len(data)
    original_bit_len = original_byte_len * 8

    # Append a single '1' bit to the message
    data += b'\x80'

    # Pad with '0' bits until message length (in bits) is congruent to 448 mod 512
    while (len(data) * 8) % 512 != 448:
        data += b'\x00'

    # Append the original length of the message as a 64-bit big-endian integer
    data += struct.pack('>Q', original_bit_len)

    # Process the message in 512-bit (64-byte) chunks
    for i in range(0, len(data), 64):
        chunk = data[i:i+64]
        w = [0] * 80

        # Break chunk into sixteen 32-bit big-endian words w[0..15]
        for j in range(16):
            w[j] = struct.unpack('>I', chunk[j*4:j*4+4])[0]

        # Extend the sixteen 32-bit words into eighty 32-bit words
        for j in range(16, 80):
            w[j] = left_rotate(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1)

        # Initialize hash value for this chunk
        a, b, c, d, e = h0, h1, h2, h3, h4

        # Main loop
        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | (~b & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= j <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xffffffff
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        # Add this chunk's hash to the result so far
        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff

    # Produce the final hash value (big-endian) as a 160-bit number
    return '{:08x}{:08x}{:08x}{:08x}{:08x}'.format(h0, h1, h2, h3, h4)

# Example usage
message = "Hello, World!"
print(f"SHA-1 hash of '{message}' is: {sha1(message.encode())}")
