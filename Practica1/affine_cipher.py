import random
import pytest
from utils import CryptographyException
from utils import prime_relative

class Affine():

    def __init__(self, alphabet, A=None, B=None):
        """
        Constructor de clase que tiene como parámetro todos los atributos
        que necesita el algoritmo de cifrado afín.
        Parámetro:
            alphabet -- el alfabeto sobre quien se cifra el mensaje.
            A -- El coeficiente A que necesita el cifrado.
            B -- El coeficiente B de desplazamiento.
        """
        self.alphabet = alphabet
        if A is not None and not prime_relative(A,len(alphabet)):
             raise CryptographyException
        self.A = A if A is not None else 1
        self.B = B if B is not None else random.randint(0,len(alphabet)-1)

    def cipher(self, message):
        """
        Cifra el mensaje recibido como parámetro con el algoritmo de
        cifrado afín, un desplazamiento sobre el alfabeto predefinido.
        Parámetro:
            message -- el mensaje a cifrar.
        """
        cipher_message = ''
        for letter in message:
            if letter in self.alphabet:
                pos = self.alphabet.find(letter)
                cipher_message += self.alphabet[((pos*self.A)+self.B)%len(self.alphabet)]
            else:
                cipher_message += letter
        return cipher_message

    def decipher(self, criptotext):
        """
        Descifra el mensaje recuperando el texto plano siempre y cuando
        haya sido cifrado con el cifrado afín.
        Parámetro:
            criptotext -- el mensaje a descifrar.
        """
        pass
