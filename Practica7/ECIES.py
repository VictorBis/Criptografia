import EllipticCurves as ec
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
        U = ec.scalar_multiplication(self.A, k, self.curve)
        V = ec.scalar_multiplication(self.B, k, self.curve)
        criptotext = []
        criptotext.append(((U[0], U[1] % 2), ord(message[0])*V[0]))
        return criptotext

    def decrypt(self, criptotext):
        pass
