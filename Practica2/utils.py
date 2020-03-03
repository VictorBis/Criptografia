from random import choice
from string import ascii_uppercase
from math import sqrt
import numpy as np
from sympy import Matrix

class CryptographyException(Exception):

    def __init__(self):
        self.message = "Invalid key"

    def __str__(self):
        return self.message

def random_string(n):
    """
    Generates a random string of lenght n
    Params:
        n - lenght of the string
    Return:
        A random string of lenght n
    """
    alphabet = ascii_uppercase
    return ''.join(choice(alphabet) for i in range(n))

def isqrt(n):
    """
    Determines if a number has an exact root
    Params:
        n - given number
    Return:
        True - n has an exact root
        False - n doesn't have an exact root
    """
    i = int(sqrt(n))
    return True if i**2 == n else False

def get_pos_array(key,alphabet):
    """
    Gets an array of positions of a string in the alphabet
    Params:
        key - word to be transformed
        alphabet - alphabet that contains the key
    Return:
        An array of positions
    """
    pos_pass = []
    for letter in key:
            pos_pass.append(alphabet.find(letter))
    return pos_pass

def generate_matrix(key,alphabet):
    """
    Generate a matrix given a key and an alphabet
    Params:
        key - key to be transformed to a matrix
        alphabet - Alphabet 
    Return:
        Matrix of positions of the given key
    """
    pos_pass = np.asarray(get_pos_array(key,alphabet))
    a = pos_pass.reshape(int(sqrt(len(key))),int(sqrt(len(key))))
    return a

def valid_det(matrix):
    """
    Validates if a matrix has a valid determinant
    Params:
        matrix - matrix to be validated
    Return:
        True - The matrix has a valid determinant
        False - The matrix doesn't have a valid determinant
    """
    return True if (np.linalg.det(matrix)) > 0 else False

def dot_matrix(matrix,alphabet,s):
    """
    Generates the string of the product of a matrix and a string in the alphabet
    Params:
        matrix - matrix to be multiplied
        alphabet - alphabet
        s - string to be multiplied
    Return:
        String of the result of the product between the matrix and the string
    """
    pos_pass = np.asarray(get_pos_array(s,alphabet))
    enciphered_vector = matrix.dot(pos_pass)%27
    res = ''
    for i in enciphered_vector:
        res += alphabet[int(i)]
    return res  

def has_inv(A,m):
    """
    Determines if a matrix has an inverse module m
    Params:
        A - Matrix
        m - module
    Return:
        True - The inverse exists
        False - The inverse doesn't exists
    """
    A = Matrix(A)
    try:
        A.inv_mod(m)
    except:
        return False
    return True

def mod_mat_inv(A,m):
    """
    Calculates the module matrix inverse
    Params:
        A - Matrix
        m - module
    Return:
        The module matrix inverse of the given matrix
    """
    A = Matrix(A)
    try:
        A = A.inv_mod(m)
    except:
        print('No')
    return np.array(A).astype(np.int32)


    
