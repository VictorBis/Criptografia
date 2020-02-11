import random
import pytest
from utils import CryptographyException

class Caesar():

    def __init__(self, alphabet, key=None):
        """
        Constructor de clase que tiene como parámetro todos los atributos
        que necesita el algoritmo de cifrado de César.
        Parámetro:
            alphabet -- el alfabeto sobre quien se cifra el mensaje.
            key -- el tamaño del desplazamiento sobre el alfabeto, si es
                   None, se debe de escoger una llave aleatoria, válida.
        """
        self.alphabet = alphabet
        if key is None:
            key = random.randint(0,len(alphabet))
        else:
            if key != key % (len(alphabet)+1):
                raise CryptographyException
        self.key = key

    def cipher(self, message, flag=None):
        """
        Cifra el mensaje recibido como parámetro con el algoritmo de
        cifrado césar, un desplazamiento sobre el alfabeto predefinido.
        Parámetro:
            message -- el mensaje a cifrar.
        """
        cipher_message = ''
        for letter in message:
            if letter in self.alphabet:
                pos = self.alphabet.find(letter)
                cipher_message += self.alphabet[(pos+self.key)%len(self.alphabet)]
            else:
                cipher_message += letter
        if flag is None:
            cipher_message = cipher_message.replace(" ","")
        return cipher_message

    def decipher(self, criptotext, flag=None):
        """
        Descifra el mensaje recuperando el texto plano siempre y cuando
        haya sido cifrado con el algoritmo de césar.
        Parámetro:
            cryptotext -- el mensaje a descifrar.
        """
        decipher_message = ''
        for letter in criptotext:
            if letter in self.alphabet:
                pos = self.alphabet.find(letter)
                decipher_message += self.alphabet[pos-self.key]
            else:
                decipher_message += letter
        if flag is None:
            decipher_message = decipher_message.replace(" ","")
        return decipher_message
