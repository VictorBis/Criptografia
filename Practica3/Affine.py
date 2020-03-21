from langdetect import detect
alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

def mod_inverse(a, m):
    """
    Obtiene el inverso multiplicativo de un número
    Parámetro:
        a -- Número del cual se desa obtener el inverso
        m -- Módulo
    """
    for x in range(1, m): 
        if ((a * x) % m == 1): 
            return x 
    return False

def decipher(criptotext):
        """
        Descifra el mensaje recuperando el texto plano siempre y cuando
        haya sido cifrado con el cifrado afín.
        El descifrado se hace por fuerza bruta.
        Parámetro:
            criptotext -- el mensaje a descifrar.
        """
        message = ''
        for A in range(0,27):
            if(A%3!=0):
                for B in range(0,28):
                    for letter in criptotext:
                        if letter in alphabet:
                            pos = alphabet.find(letter)
                            inverse = mod_inverse(A,len(alphabet))
                            message += alphabet[((inverse*(pos-B))%len(alphabet))]
                        else:
                            message += letter
                    if(detect(message.lower())=='es'):
                        print('A:{} B:{} - {} \n'.format(A,B,message.lower()))
                    message = ''

if __name__ == "__main__":
    with open('Three.txt', 'r') as file:
        message = file.read().replace('\n', '')
    decipher(message)
