import string

def caesar_cipher(text, shift=3):
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    result = []
    for char in text:
        if char in alphabet_lower:
            result.append(alphabet_lower[(alphabet_lower.index(char) + shift) % 26])
        elif char in alphabet_upper:
            result.append(alphabet_upper[(alphabet_upper.index(char) + shift) % 26])
        else:
            result.append(char)
    return ''.join(result)

with open('plaintext.txt', 'w') as f:
    f.write('Hello, World!\nThis is a secret message.\nPython encryption test 322.')

with open('plaintext.txt', 'r') as f:
    content = f.read()
    encrypted = caesar_cipher(content)
    print("Encrypted text:")
    print(encrypted)
    with open('ciphertext.txt', 'w') as out_f:
        out_f.write(encrypted)