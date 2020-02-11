def cipher(message):
    """
    Cifra el mensaje recibido como parámetro con el algoritmo de cifrado
    XOR.
    Parámetro:
       message -- el mensaje a cifrar.
    """
    return ''.join([chr(ord(letter)^1) for letter in message])
    
def decipher(criptotext):
    """
    Descifra el mensaje recuperando el texto plano siempre y cuando haya
    sido cifrado con XOR.
    Parámetro:
       cryptotext -- el mensaje a descifrar.
    """
    return ''.join([chr(ord(letter)^1) for letter in criptotext])
