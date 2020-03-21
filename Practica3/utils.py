from math import sqrt
import numpy as np
from sympy import Matrix

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


def dot_matrix(A,alphabet,s):
    """
    Generates the string of the product of a matrix and a string in the alphabet
    Params:
        A - matrix to be multiplied
        alphabet - alphabet
        s - string to be multiplied
    Return:
        String of the result of the product between the matrix and the string
    """
    pos_pass = np.asarray(get_pos_array(s,alphabet))
    enciphered_vector = A.dot(pos_pass)%26
    res = ''
    for i in enciphered_vector:
        res += alphabet[int(i)]
    return res  

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
    A = A.inv_mod(m)
    return np.array(A).astype(np.int32)


    
