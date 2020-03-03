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

def get_pos_array(key,alphabet):
    pos_pass = []
    for letter in key:
            pos_pass.append(alphabet.find(letter))
    return pos_pass

def generate_matrix(key,alphabet):
    pos_pass = np.asarray(get_pos_array(key,alphabet))
    a = pos_pass.reshape(int(sqrt(len(key))),int(sqrt(len(key))))
    return a

def valid_det(matrix):
    return True if (np.linalg.det(matrix)) > 0 else False

def dot_matrix(matrix,alphabet,s):
    pos_pass = np.asarray(get_pos_array(s,alphabet))
    enciphered_vector = matrix.dot(pos_pass)%27
    res = ''
    for i in enciphered_vector:
        res += alphabet[int(i)]
    return res  

    
