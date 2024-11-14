import random

def generate_prime_and_base():
    # In a real-world application, you would use a larger prime number and a secure method to generate it.
    # Here, we use a small prime for demonstration purposes.
    prime = 23  # A small prime number
    base = 5    # A primitive root modulo prime
    return prime, base

def power_mod(base, exponent, modulus):
    """Computes (base ** exponent) % modulus using modular exponentiation."""
    return pow(base, exponent, modulus)

def diffie_hellman():
    # Step 1: Generate a prime number and base
    prime, base = generate_prime_and_base()
    
    # Step 2: Alice chooses a private key (a) and computes her public key (A)
    alice_private_key = random.randint(1, prime - 1)
    alice_public_key = power_mod(base, alice_private_key, prime)
    
    # Step 3: Bob chooses a private key (b) and computes his public key (B)
    bob_private_key = random.randint(1, prime - 1)
    bob_public_key = power_mod(base, bob_private_key, prime)
    
    # Step 4: Exchange public keys (A and B)
    print(f"Alice's Public Key: {alice_public_key}")
    print(f"Bob's Public Key: {bob_public_key}")
    
    # Step 5: Compute the shared secret
    alice_shared_secret = power_mod(bob_public_key, alice_private_key, prime)
    bob_shared_secret = power_mod(alice_public_key, bob_private_key, prime)
    
    # Step 6: Verify that both shared secrets are the same
    assert alice_shared_secret == bob_shared_secret, "Shared secrets do not match!"
    
    return alice_shared_secret

if __name__ == "__main__":
    shared_secret = diffie_hellman()
    print(f"Shared Secret: {shared_secret}")