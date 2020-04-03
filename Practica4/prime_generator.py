from random import randint
from random import randrange
from factorial import factorial as fac

def big_int(size=None):
    """
    Generador de números aleatorios de un tamaño fijo recibido como parámetro, si el parámetro es
    menor que 100 o None, entonces la función no le hace caso y genera uno de tamaño arbitrario,
    máximo es de 150 dígitos.
    :return: Un número del tamaño descrito.
    """
    if size is None or size < 100:
        size = randint(100,150)
    return randint(10**(size-1),(10**size)-1)

def miller_rabin(n):
    """
    Implementación del test de primalidad de Miller-Rabin.
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    if n == 2 or n == 3:
        return True
    k = 2
    r, d = 0, n-1
    while d%2 == 0: #Factorizar las potencias de 2 de n-2
        d //= 2
        r += 1
        
    for _ in range(k):
        a = randrange(2, n-1)
        x = pow(a, d, n)
        if x != 1 and x != n-1:
            for _ in range(r-1):
                x = pow(x, 2, n)
                if x == n-1:
                    break
            else:
                return False
    return True


def wilson(n):
    """
    Implementaión del test de primalidad de Wilson, basado en el teorema de Wilson,
    (p-1)! ≡ -1 mod p
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    return fac(n-1)%n+1 == n