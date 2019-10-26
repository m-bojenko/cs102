def encrypt_caesar(plaintext: str) -> str:
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in range(0, len(plaintext)):
        if 64 < ord(plaintext[i]) < 88 or 96 < ord(plaintext[i]) < 120:
            ciphertext = ciphertext + chr(ord(plaintext[i]) + 3)
        elif 87 < ord(plaintext[i]) < 91 or 119 < ord(plaintext[i]) < 123:
            ciphertext = ciphertext + chr(ord(plaintext[i]) - 23)
        else:
            ciphertext = ciphertext + plaintext[i]
    return ciphertext


def decrypt_caesar(ciphertext: str) -> str:
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in range(0, len(ciphertext)):
        if 67 < ord(ciphertext[i]) < 91 or 99 < ord(ciphertext[i]) < 123:
            plaintext = plaintext + chr(ord(ciphertext[i]) - 3)
        elif 64 < ord(ciphertext[i]) < 68 or 96 < ord(ciphertext[i]) < 100:
            plaintext = plaintext + chr(ord(ciphertext[i]) + 23)
        else:
            plaintext = plaintext + ciphertext[i]
    return plaintext
