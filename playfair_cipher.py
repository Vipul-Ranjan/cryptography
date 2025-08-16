def normalize_text(s: str) -> str:
    """Lowercase, keep letters only, replace 'j' with 'i' (Playfair convention)."""
    s = s.lower()
    s = "".join(ch for ch in s if ch.isalpha())
    return s.replace("j", "i")

def generate_key_square(key: str) -> list:
    """
    Build a 5x5 key square from the key.
    Steps:
      - normalize key (lowercase, letters only, j->i)
      - append remaining unused letters of alphabet (skip 'j')
      - split into 5 rows of 5 letters each
    """
    key = normalize_text(key)
    seen = set()
    key_letters = []
    for ch in key:
        if ch not in seen:
            seen.add(ch)
            key_letters.append(ch)
    for ch in "abcdefghijklmnopqrstuvwxyz":
        if ch == "j":  # Playfair merges 'i' and 'j'
            continue
        if ch not in seen:
            seen.add(ch)
            key_letters.append(ch)
    # make 5x5 matrix (list of 5 lists)
    key_square = [key_letters[i*5:(i+1)*5] for i in range(5)]
    return key_square

def find_position(ch: str, key_square: list) -> tuple:
    """Return (row, col) of character ch in key_square."""
    for r in range(5):
        for c in range(5):
            if key_square[r][c] == ch:
                return r, c
    raise ValueError(f"Character {ch!r} not found in key square")

def prepare_plaintext(plaintext: str, filler: str = "x") -> list:
    """
    Turn plaintext into digraphs (pairs) according to Playfair rules:
      - remove non-letters and lowercase (normalize_text)
      - replace 'j' with 'i'
      - split into pairs
      - if both letters in a pair are same, insert filler after the first
      - if one final letter remains, pair it with filler
    """
    text = normalize_text(plaintext)
    digraphs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else ""
        if b == "":
            digraphs.append(a + filler)
            i += 1
        elif a == b:
            digraphs.append(a + filler)
            i += 1
        else:
            digraphs.append(a + b)
            i += 2
    return digraphs

def encrypt_pair(pair: str, key_square: list) -> str:
    a, b = pair[0], pair[1]
    row_a, col_a = find_position(a, key_square)
    row_b, col_b = find_position(b, key_square)
    if row_a == row_b:  # same row -> replace each by letter to the right
        return key_square[row_a][(col_a + 1) % 5] + key_square[row_b][(col_b + 1) % 5]
    elif col_a == col_b:  # same column -> replace each by letter below
        return key_square[(row_a + 1) % 5][col_a] + key_square[(row_b + 1) % 5][col_b]
    else:  # rectangle -> swap columns
        return key_square[row_a][col_b] + key_square[row_b][col_a]

def decrypt_pair(pair: str, key_square: list) -> str:
    a, b = pair[0], pair[1]
    row_a, col_a = find_position(a, key_square)
    row_b, col_b = find_position(b, key_square)
    if row_a == row_b:  # same row -> letter to the left
        return key_square[row_a][(col_a - 1) % 5] + key_square[row_b][(col_b - 1) % 5]
    elif col_a == col_b:  # same column -> letter above
        return key_square[(row_a - 1) % 5][col_a] + key_square[(row_b - 1) % 5][col_b]
    else:  # rectangle -> swap columns
        return key_square[row_a][col_b] + key_square[row_b][col_a]

def encrypt(plaintext: str, key: str) -> str:
    ks = generate_key_square(key)
    pairs = prepare_plaintext(plaintext)
    cipher = "".join(encrypt_pair(p, ks) for p in pairs)
    return cipher.upper()

def decrypt(ciphertext: str, key: str) -> str:
    ks = generate_key_square(key)
    pairs = [ciphertext[i:i+2].lower() for i in range(0, len(ciphertext), 2)]
    plain = "".join(decrypt_pair(p, ks) for p in pairs)
    return plain

# Example usage (if run as a script)
if __name__ == "__main__":
    key = "playfair example"
    plaintext = "Hide the gold in the tree stump"
    ks = generate_key_square(key)
    for row in ks:
        print(" ".join(row))
    print("Prepared digraphs:", prepare_plaintext(plaintext))
    print("Ciphertext:", encrypt(plaintext, key))
    print("Decrypted back:", decrypt(encrypt(plaintext, key), key))
