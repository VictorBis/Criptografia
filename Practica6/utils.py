from random import randrange


def prime_relative(a, b):
    if(b == 0):
        return a == 1
    else:
        return prime_relative(b, a % b)


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


def mcd(a, b):
    """
    Calcula el mcd de a y b
    Params:
        a - número a
        b - nñumero b
    Return:
        El máximo común divisor de a y b
    """
    if b == 0:
        return a
    else:
        return mcd(b, a % b)


def choose_e(phi):
    """
    Elige un número e, tal que 1 < e < phi y mcd(e,phi) = 1
    Params:
        phi - resultado de calcular (p-1)*(q-1)
    Return:
        e - número > 1 y < phi, tal que mcd(e,phi) = 1 
    """
    e = randrange(2, phi)
    while (mcd(e, phi) != 1):
        e = randrange(2, phi)
    return e


def factorial(n):
    """
Calcula el factorial de un numero
Se calcula el factorial reduciendo la multiplicacion en factoriales a la mitad

Para mas informacion acerca del algoritmo, consultar:
https://sites.google.com/site/examath/research/factorials
    """
    if n == 1 or n == 0:
        return 1

    is_odd = False
    upto_n = n

    if n & 1 == 1:
        upto_n -= 1
        is_odd = True

    next_sum = upto_n
    next_multi = upto_n
    factorial = 1

    while next_sum >= 2:
        factorial *= next_multi
        next_sum -= 2
        next_multi += next_sum

    if is_odd:
        factorial *= n

    return factorial
