class Vigenere():

    def __init__(self, alphabet, password=None):
        #Recomendación, ingeniárselas para no cargar siempre O(n^2) en memoria aunque esto no
        #será evaluado, con n el tamaño del alfabeto.
        """
        Constructor de clase, recibe un parámetro obligatorio correspondiente al alfabeto
        y un parámetro opcional que es la palabra clave, en caso de ser None, entonces
        generar una palabra pseudoaleatoria de al menos tamaño 4.
        :param alphabet: Alfabeto a trabajar con el cifrado.
        :param password: El password que puede ser o no dada por el usuario.
        """
        self.alphabet = alphabet
        if password is None:
            self.password = 'PASS'
        else:
            self.password = password

    def cipher(self, message):
        """
        Usando el algoritmo de cifrado de vigenere, cifrar el mensaje recibido como parámetro,
        usando la tabla descrita en el PDF.
        :param message: El mensaje a cifrar.
        :return: Una cadena de texto con el mensaje cifrado.
        """
        ciphered = ""
        pos_pass = [] #positions of every char of the password in the alphabet
        for letter in self.password:
            pos_pass.append(self.alphabet.find(letter))
        i = 0
        for letter in message:
            pos = (self.alphabet.find(letter) + pos_pass[i%len(self.password)]) % 27
            ciphered += self.alphabet[pos]
            i +=1
        return ciphered



    def decipher(self, ciphered):
        """
        Implementación del algoritmo de decifrado, según el criptosistema de vigenere.
        :param ciphered: El criptotexto a decifrar.
        :return: El texto plano correspondiente del parámetro recibido.
        """
        message = ""
        pos_pass = [] #positions of every char of the password in the alphabet
        for letter in self.password:
            pos_pass.append(self.alphabet.find(letter))
        i = 0
        for letter in ciphered:
            pos = (self.alphabet.find(letter) - pos_pass[i%len(self.password)] + 27) %27
            message += self.alphabet[pos]
            i +=1
        return message