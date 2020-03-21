alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

def decipher(criptotext):
    """
        Descifra el mensaje recuperando el texto plano siempre y cuando
        haya sido cifrado con el algoritmo de césar.
        Decifra por medio de fuerza bruta, imprimiendo todos los resultados obtenidos.
        Parámetro:
            cryptotext -- el mensaje a descifrar.
        """
    message = ''
    for i in range(0,len(alphabet)):
        for m in criptotext:
            if m in alphabet:
                pos = alphabet.find(m)
                message += alphabet[pos-i]
            else:
                message += m
        print('Key {}: {} \n'.format(i,message.lower()))
        message = ''

if __name__ == "__main__":
    with open('Two.txt', 'r') as file:
        message = file.read()
    decipher(message)
