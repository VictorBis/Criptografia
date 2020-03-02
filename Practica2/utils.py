from random import choice
from string import ascii_uppercase
from math import sqrt
import numpy as np

class CryptographyException(Exception):

    def __init__(self):
        self.message = "Invalid key"

    def __str__(self):
        return self.message

def random_string(n):
    alphabet = ascii_uppercase
    return ''.join(choice(alphabet) for i in range(n))

def isqrt(n):
    i = int(sqrt(n))
    return True if i**2 == n else False

def generate_matrix(key,alphabet):
    pos_pass = []
    for letter in key:
            pos_pass.append(alphabet.find(letter))
    pos_pass = np.asarray(pos_pass)
    a = pos_pass.reshape(int(sqrt(len(key))),int(sqrt(len(key))))
    return a

def valid_det(matrix):
    return True if (np.linalg.det(matrix)) > 0 else False
    
