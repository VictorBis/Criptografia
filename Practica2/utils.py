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

#Desde aquí
def modMatInv(A,p):       # Finds the inverse of matrix A mod p
  n=len(A)
  A=np.array(A)
  adj=np.zeros(shape=(n,n))
  for i in range(0,n):
    for j in range(0,n):
      adj[i][j]=((-1)**(i+j)*int(round(np.linalg.det(minor(A,j,i)))))%p
  return (modInv(int(round(np.linalg.det(A))),p)*adj)%p

def modInv(a,p):          # Finds the inverse of a mod p, if it exists
  for i in range(1,p):
    if (i*a%p)==1:
      return i
  return ValueError("NO")

def minor(A,i,j):    # Return matrix A with the ith row and jth column deleted
  A=np.array(A)
  minor=np.zeros(shape=(len(A)-1,len(A)-1))
  p=0
  for s in range(0,len(minor)):
    if p==i:
      p=p+1
    q=0
    for t in range(0,len(minor)):
      if q==j:
        q=q+1
      minor[s][t]=A[p][q]
      q=q+1
    p=p+1
  return minor


    
