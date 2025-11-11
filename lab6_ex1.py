class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def caesar(str: str, offset: int) -> str:
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

    print("=" * 50)
    print(f"{Colors.BOLD}Exercise 1 - Caesar Cipher Warm-Up{Colors.RESET}")
    print("=" * 50)

    ciphertext = caesar(str, offset);
    print(f"Inputs: {Colors.GREEN}s= '{str}', k= {offset}{Colors.RESET}")
    print(f"Output: {Colors.RED}'{ciphertext}'{Colors.RESET}\n")

    print(f"Put the output into caesar again but with -offset to see if reverse works..\n")
    original_recovered = caesar(ciphertext, -offset)
    print(f"Inputs: {Colors.GREEN}s= '{ciphertext}', k= {-offset}{Colors.RESET}")
    print(f"Output: {Colors.RED}'{original_recovered}'{Colors.RESET}")
