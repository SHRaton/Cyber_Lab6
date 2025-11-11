import hashlib
import os

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def compute_sha256(filepath: str) -> str:
    sha256_hash = hashlib.sha256()

    # 'rb' is to open the file in read binary mode
    with open(filepath, 'rb') as f:
        file_content = f.read()
        sha256_hash.update(file_content)

    return sha256_hash.hexdigest()


def create_sample_file(filepath: str):
    if not os.path.exists(filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("This is a random file sample")
        print(f"Created sample file: {filepath}")


def flip_one_character(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if len(content) == 0:
        print("File is empty, cannot flip character")
        return

    # Flip the first character
    modified_content = list(content)
    if modified_content[0].isupper():
        modified_content[0] = modified_content[0].lower()
    elif modified_content[0].islower():
        modified_content[0] = modified_content[0].upper()
    else:
        # If not a letter replace with 'X'
        modified_content[0] = 'X'

    # Write back the modified content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(''.join(modified_content))

    print("Modified: Flipped first character in the file")


if __name__ == "__main__":
    filename = "data.txt"

    print("=" * 50)
    print(f"{Colors.BOLD}Exercise 2 - SHA-256 File Integrity Check{Colors.RESET}")
    print("=" * 50)

    # If data.txt doesn't exist => generate it
    create_sample_file(filename)

    # Read file and compute initial hash
    print()
    print(f"{Colors.BOLD}Step 1:{Colors.RESET} Computing initial SHA-256 hash")
    try:
        hash1 = compute_sha256(filename)
        print(f"Original SHA-256: {Colors.CYAN}{hash1}{Colors.RESET}")
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        exit(1)

    # Prompt user to edit file
    print()
    print(f"{Colors.BOLD}Step 2:{Colors.RESET} File modification")
    choice = input(f"Choose option:\n  {Colors.GREEN}1) Manual edit (you edit the file by yourself){Colors.RESET}\n  {Colors.RED}2) Auto flip (program changes 1 char){Colors.RESET}\nChoice [1/2]: ")

    if choice == "1":
        input(f"\nPlease edit {filename} now and press ENTER when done...")
    elif choice == "2":
        flip_one_character(filename)
    else:
        print(f"Error: Choice {choice} don't exist")
        exit(1)

    # Recompute hash after modification
    print()
    print(f"{Colors.BOLD}Step 3:{Colors.RESET} Recomputing SHA-256 after modification...")
    hash2 = compute_sha256(filename)
    print(f"Modified SHA-256: {Colors.MAGENTA}{hash2}{Colors.RESET}")

    # Print the two hashes to compare
    print()
    print("=" * 50)
    print("File Integrity Check Result:")
    print("=" * 50)

    if hash1 == hash2:
        print("MATCH: The file has NOT been modified (Digests are identical)")
    else:
        print("MISMATCH: The file HAS been modified (Digests are completely different)")
        print()
        print(f"- Original:  {Colors.CYAN}{hash1}{Colors.RESET}")
        print(f"- Modified:  {Colors.MAGENTA}{hash2}{Colors.RESET}")

    print("=" * 50)