from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def aes_encrypt(plaintext, key):
    
    cipher = AES.new(key, AES.MODE_CBC)
    
    ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    return cipher.iv + ciphertext  

def aes_decrypt(ciphertext, key):
    
    iv = ciphertext[:AES.block_size]
    ciphertext = ciphertext[AES.block_size:]
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode('utf-8')


key = get_random_bytes(16)  
plaintext = "This is a secret message."


ciphertext = aes_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)


decrypted_text = aes_decrypt(ciphertext, key)
print("Decrypted:", decrypted_text)
