# lab6_ex3.py
# Exercise 3 — AES-GCM Toy Locker (Library Use)
# Goal: Use authenticated encryption with AES-GCM

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# ANSI color codes for terminal output
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


def encrypt_bytes(key: bytes, plaintext_bytes: bytes) -> tuple:
    # Generate a fresh random 12-byte nonce (CRITICAL: must be unique per encryption)
    nonce = get_random_bytes(12)
    # Create AES cipher in GCM mode
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    # Encrypt and generate authentication tag in one step
    ciphertext, tag = cipher.encrypt_and_digest(plaintext_bytes)

    return (nonce, ciphertext, tag)


def decrypt_bytes(key: bytes, nonce: bytes, ciphertext: bytes, tag: bytes) -> bytes:
    # Create AES cipher in GCM mode with the same nonce
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    
    # Decrypt and verify authentication tag
    # If tag doesn't match, raises ValueError
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    
    return plaintext


def print_separator(char='=', length=70):
    """Prints a visual separator line."""
    print(char * length)

def decryption_error_tests(key: bytes, nonce: bytes, ciphertext: bytes, tag: bytes):
    # Test 1: Flip one bit in the ciphertext
    print(f"{Colors.MAGENTA}Test 1: Tampering with ciphertext{Colors.RESET}")
    tampered_ciphertext = bytearray(ciphertext)
    if len(tampered_ciphertext) > 0:
        # Flip the first bit of the first byte
        tampered_ciphertext[0] ^= 0x01
        tampered_ciphertext = bytes(tampered_ciphertext)
        print(f"Original ciphertext:  {ciphertext.hex()}")
        print(f"Tampered ciphertext:  {tampered_ciphertext.hex()}")

        try:
            decrypted = decrypt_bytes(key, nonce, tampered_ciphertext, tag)
            print(f"{Colors.RED}WARNING: Tampered data was decrypted (should not happen!){Colors.RESET}")
        except ValueError as e:
            print(f"{Colors.GREEN}Tampering detected! Error: {e}{Colors.RESET}")

    print()

    # Test 2: Flip one bit in the authentication tag
    print(f"{Colors.MAGENTA}Test 2: Tampering with authentication tag{Colors.RESET}")
    tampered_tag = bytearray(tag)
    # Flip the last bit of the last byte
    tampered_tag[-1] ^= 0x01
    tampered_tag = bytes(tampered_tag)
    print(f"Original tag:  {tag.hex()}")
    print(f"Tampered tag:  {tampered_tag.hex()}")

    try:
        decrypted = decrypt_bytes(key, nonce, ciphertext, tampered_tag)
        print(f"{Colors.RED}WARNING: Tampered tag was accepted (should not happen!){Colors.RESET}")
    except ValueError as e:
        print(f"{Colors.GREEN}Tampering detected! Error: {e}{Colors.RESET}")

    print()

    # Test 3: Wrong key
    print(f"{Colors.MAGENTA}Test 3: Decrypting with wrong key{Colors.RESET}")
    wrong_key = get_random_bytes(32)
    print(f"Using different key: {wrong_key.hex()[:16]}...")

    try:
        decrypted = decrypt_bytes(wrong_key, nonce, ciphertext, tag)
        print(f"{Colors.RED}WARNING: Wrong key was accepted (should not happen!){Colors.RESET}")
    except ValueError as e:
        print(f"{Colors.GREEN}Wrong key detected! Error: {e}{Colors.RESET}")

def main():
    print_separator()
    print(f"{Colors.BOLD}Exercise 3 — AES-GCM Toy Locker{Colors.RESET}")
    print_separator()
    print()


    print(f"{Colors.BOLD}Step 1:{Colors.RESET} Generating random 32-byte key (AES-256)")
    key = get_random_bytes(32)
    print(f"Key (hex): {key.hex()}")
    print(f"Key length: {len(key)} bytes")
    print()


    print(f"{Colors.BOLD}Step 2:{Colors.RESET} Encrypting message")
    original_message = b"lab secret"
    print(f"Original message: {Colors.BOLD}{original_message}{Colors.RESET}")

    nonce, ciphertext, tag = encrypt_bytes(key, original_message)

    print(f"\n{Colors.GREEN}Encryption successful!{Colors.RESET}")
    print(f"  Nonce length:      {len(nonce)} bytes")
    print(f"  Ciphertext length: {len(ciphertext)} bytes")
    print(f"  Tag length:        {len(tag)} bytes")
    print()
    print(f"  Nonce (hex):      {nonce.hex()}")
    print(f"  Ciphertext (hex): {ciphertext.hex()}")
    print(f"  Tag (hex):        {tag.hex()}")
    print()


    print(f"{Colors.BOLD}Step 3:{Colors.RESET} Decrypting message")
    try:
        decrypted_message = decrypt_bytes(key, nonce, ciphertext, tag)
        print(f"{Colors.GREEN}Decryption successful!{Colors.RESET}")
        print(f"Recovered message: {Colors.BOLD}{decrypted_message}{Colors.RESET}")

        # Verify integrity
        if decrypted_message == original_message:
            print(f"{Colors.GREEN}Integrity verified: Original == Decrypted{Colors.RESET}")
        else:
            print(f"{Colors.RED}Integrity check failed!{Colors.RESET}")
    except ValueError as e:
        print(f"{Colors.RED}Decryption failed: {e}{Colors.RESET}")

    print()

    # Step 4: Demonstrate tampering detection
    print_separator('-')
    print(f"{Colors.YELLOW}Step 4: Testing tampering detection{Colors.RESET}")
    print_separator('-')
    print()

    decryption_error_tests(key, nonce, ciphertext, tag)


if __name__ == "__main__":
    main()