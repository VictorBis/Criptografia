import EllipticCurves
from random import randint


class ECIES():

    def __init__(self, curve, A, B, N, s, p):
        self.curve = curve
        self.A = A
        self.B = B
        self.N = N
        self.s = s
        self.p = p

    def encrypt(self, message):
        k = randint(1, self.N - 1)
        U = k * self.A
        V = k * self.B

    def decrypt(self, criptotext):
        pass
