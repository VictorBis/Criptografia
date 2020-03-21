from utils import *

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def decipher(ciphered,key,n):
    """
    Usando el algoritmo de decifrado, recibiendo una cadena que se asegura que fue cifrada
    previamente con el algoritmo de Hill, obtiene el texto plano correspondiente.
    :param ciphered: El criptotexto de algún mensaje posible.
    :return: El texto plano correspondiente a manera de cadena.
    """
    cipher = ''
    seg = ''
    matrix = generate_matrix(key,alphabet)
    mat_inv = mod_mat_inv(matrix,len(alphabet)) 
    for i in range(0,len(ciphered),int(sqrt(n))):
        seg += ciphered[i:i+int(sqrt(n))]
        cipher += dot_matrix(mat_inv,alphabet,seg)
        seg = ''
    return cipher

if __name__ == "__main__":
    with open('Four.txt', 'r') as file:
        message = file.read().replace('\n', '')
    key = 'FZHC'
    n = 4
    print(decipher(message,key,n).lower())