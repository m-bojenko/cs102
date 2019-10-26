def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    keyword = (len(plaintext) // len(keyword)) * keyword
    for i in range(0, len(plaintext) % len(keyword)):
        keyword = keyword + keyword[i]
    ciphertext = ""
    for i in range(0, len(plaintext)):
        if 64 < ord(plaintext[i]) < 91:
            if ord(keyword[i]) - 65 > 90 - ord(plaintext[i]):
                ciphertext = ciphertext + chr(64 + ord(keyword[i]) - 65 - (90 - ord(plaintext[i])))
            else:
                ciphertext = ciphertext + chr(ord(plaintext[i]) + ord(keyword[i]) - 65)
        if 96 < ord(plaintext[i]) < 123:
            if ord(keyword[i]) - 97 > 122 - ord(plaintext[i]):
                ciphertext = ciphertext + chr(96 + ord(keyword[i]) - 97 - (122 - ord(plaintext[i])))
            else:
                ciphertext = ciphertext + chr(ord(plaintext[i]) + ord(keyword[i]) - 97)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    keyword = (len(ciphertext) // len(keyword)) * keyword
    for i in range(0, len(ciphertext) % len(keyword)):
        keyword = keyword + keyword[i]
    plaintext = ""
    for i in range(0, len(ciphertext)):
        if 64 < ord(ciphertext[i]) < 91:
            if ord(keyword[i]) > ord(ciphertext[i]):
                plaintext = plaintext + chr(91 - (ord(keyword[i]) - ord(ciphertext[i])))
            else:
                plaintext = plaintext + chr(ord(ciphertext[i]) - (ord(keyword[i]) - 65))
        if 96 < ord(ciphertext[i]) < 123:
            if ord(keyword[i]) > ord(ciphertext[i]):
                plaintext = plaintext + chr(123 - (ord(keyword[i]) - ord(ciphertext[i])))
            else:
                plaintext = plaintext + chr(ord(ciphertext[i]) - (ord(keyword[i]) - 97))
    return plaintext
