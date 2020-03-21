from utils import get_pos_array

alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

def decipher(ciphered,password):
        """
        Implementación del algoritmo de decifrado, según el criptosistema de vigenere.
        Param: 
            ciphered: El criptotexto a decifrar.
        Return: 
            El texto plano correspondiente del parámetro recibido.
        """
        message = ""
        pos_pass = get_pos_array(password,alphabet)
        i = 0
        for letter in ciphered:
            if letter in alphabet:
                pos = (alphabet.find(letter) - pos_pass[i%len(password)] + 27) %27
                message += alphabet[pos]
                i +=1
            else:
                message += letter
        return message

if __name__ == "__main__":
    with open('One.txt', 'r') as file:
        message = file.read()
    print(decipher(message,'INFANTE').lower())