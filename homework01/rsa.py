import random


def is_prime(n: int) -> bool:
    """
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    k = 0
    for i in range(1, n):
        if n % i == 0:
            k += 1
    if k == 1:
        return True
    else:
        return False


def gcd(a, b):
    """
    Euclid's algorithm for determining the greatest common divisor.
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    while a != b:
        if (a > b):
            a = a - b
        elif (b > a):
            b = b - a
    return a


def multiplicative_inverse(e, phi):
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.
    >>> multiplicative_inverse(7, 40)
    23
    """
    a = phi
    b = e
    mas = [[a, b, a % b, a // b, 0, 0]]
    k = 0
    while True:
        a = b
        b = mas[k][2]
        mas.extend([a, b, a % b, a // b, 0, 0])
        k += 1
        if a % b == 0:
            break
    mas[k][4] = 0
    mas[k][5] = 1
    for i in range(k - 1, 0, -1):
        mas[i][4] = mas[i + 1][5]
        mas[i][5] = mas[i + 1][4] - mas[i + 1][5] * (mas[i][0] // mas[i][1])
    return mas[0][5] % phi


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    # n = pq
    n = p * q

    # phi = (p-1)(q-1)
    phi = (p - 1)(q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)
