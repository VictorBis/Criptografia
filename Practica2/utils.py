import random
import string
class CryptographyException(Exception):

    def __init__(self):
        self.message = "Invalid key"

    def __str__(self):
        return self.message

def random_string(n):
    alphabet = string.ascii_uppercase
    return ''.join(random.choice(alphabet) for i in range(n))
