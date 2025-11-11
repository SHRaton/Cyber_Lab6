
def caesar(tr: str, offset: int) -> str:
    output = []

    offset = offset % 26 

    for ch in str:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shifted_pos = (ord(ch) - base + offset) % 26
            output.append(chr(base + shifted_pos))
        else:
            output.append(ch)
    return ''.join(output)

if __name__ == "__main__":
    str = "Hello World!";
    offset = 5;

    ciphertext = caesar(str, offset);
    print(f"Original: {str}")
    print(f"Décalage offset: {offset}: {ciphertext}")
    # Expected output: Mjqqt, Btwqi!

    # 2. Déchiffrement (avec -k)
    original_recovered = caesar(ciphertext, -k)
    print(f"Décalage -offset= {-offset}: {original_recovered}")

    # 3. Vérification
    check = original_recovered == str
    print(f"Vérification caesar(caesar(str, offset), -offset) == str: {check}")