from prime_generator import generate_prime
from utils import choose_e
from sympy import mod_inverse


class RSA():

    def __init__(self):
        """
        Constructor de RSA, aquí se deben de generar los primos p y q
        para que puedan ser vistos por toda la clase, así como la llave
        pública y privada.
        """
        # Aquí también deben de generar su priv_key y pub_key
        self.p = generate_prime()
        self.q = generate_prime()
        self.n = self.p*self.q
        self.pub_key = choose_e(self.__phi__())
        self.priv_key = mod_inverse(self.pub_key, self.__phi__())
        self.padding_scheme = False

        # Se esciben pub_key y priv_key
        f_public = open('pub_key.pem', 'w')
        f_public.write(str(self.n) + '\n')
        f_public.write(str(self.pub_key) + '\n')
        f_public.close()

        f_private = open('priv_key.pem', 'w')
        f_private.write(str(self.n) + '\n')
        f_private.write(str(self.priv_key) + '\n')
        f_private.close()

    def __phi__(self):
        """
        Función completamente privada y auxiliar, únicamente para el uso de las
        pruebas unitarias.
        :return: el número de primos relativos con n.
        """
        return (self.p - 1) * (self.q - 1)

    def encrypt(self, message):
        """
        Encripta un mensaje recibido como parámetro y lo regresa a manera
        de lista de enteros.
        :param message: el mensaje a encriptar.
        :return: una lista de enteros con el mensaje encriptado.
        """
        cipher = []
        for m in message:
            cipher.append(pow(ord(m), self.pub_key, self.n))
        return cipher

    def decrypt(self, criptotext):
        """
        Desencripta un criptotexto cifrado con RSA y lo regresa a manera
        de cadena, recuperando la información del mensaje original.
        :param criptotext: el mensaje recibido que se va a desencriptar.
        :return: una cadena con el mensaje original.
        """
        message = ''
        for i in criptotext:
            message += chr(pow(i, self.priv_key, self.n))
        return message
