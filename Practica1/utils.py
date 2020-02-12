class CryptographyException(Exception):

    def __init__(self):
        self.message = "Invalid key"

    def __str__(self):
        return self.message

def prime_relative(a, b):
    if b == 0:
        return a == 1
    else:
        return prime_relative(b, a % b)

def mod_inverse(a, m): 
    a = a % m
    for x in range(1, m): 
        if ((a * x) % m == 1): 
            return x 
    return 1
