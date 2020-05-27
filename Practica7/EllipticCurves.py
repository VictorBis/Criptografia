from sympy import mod_inverse


class Curve():

    def __init__(self, A, B, p):
        """
        Construcutor de clase que va a representar a la curva elíptica de la
        forma y^2 = x^3 + Ax + B (mod p).
        :param A: primer coeficiente de la curva.
        :param B: segundo coeficiente de la curva.
        :param p: el tamaño del campo sobre el cual se hace la curva.
        """
        self.A = A
        self.B = B
        self.p = p

    def is_on_curve(self, point):
        """
        Método de clase regresa true si un punto está en la curva, éste punto
        está representado a manera de tupla, como (x, y).
        :param point: Una tupla de enteros representando a un punto.
        :return: true si el punto está en la curva, false en otro caso.
        """
        if point is None:
            return True
        else:
            return pow(point[1], 2) % self.p == (pow(point[0], 3) + self.A*point[0] + self.B) % self.p

    def determinant(self):
        """
        Regresa el determinante de una curva, recordando que su determinante
        es calculado de la forma 4A^3 + 27B^2.
        :return: El entero con el valor del determinante.
        """
        return 4*pow(self.A, 3) + 27*pow(self.B, 2)


def add_points(p, q, curve):
    """
    Dados un par de puntos y una curva elíptica, calcula el punto de la suma
    bajo la curva elíptica recibida como parámetro, se asume que p y q ya
    forman parte de la curva.
    :param p: una tupla representando un punto de la curva.
    :param q: una tupla representando un punto de la curva.
    :param curve: una instancia de la clase de este script.
    :return: Una tupla que contiene el resultado de la suma o None en caso de
    que haya sido evaluada al punto infinito.
    """
    if p[0] == q[0] and -p[1] % curve.p == q[1]:
        return None
    else:
        lam = 0
        if p == q:
            lam = (3*pow(p[0], 2) + curve.A)*mod_inverse(2*p[1], curve.p)
        else:
            lam = (p[1] - q[1]) * mod_inverse(p[0] - q[0], curve.p)
        x3 = pow(lam, 2) - p[0] - q[0]
        y3 = lam*(p[0]-x3) - p[1]
        return (x3, y3)


def scalar_multiplication(p, k, curve):
    """
    Dado un escalar del campo, k, calcula el punto kP bajo la definición
    de curvas elípticas.
    :param p: una tupla representando un punto de la curva.
    :param k: el escalar a multiplicar por el punto.
    :param curve: la curva sobre la cual se calculan las operaciones.
    :return: una tupla representando a kP o None si al sumar ese punto cayó
    en algún momento al punto infinito.
    """
    return p if k == 1 else (add_points(p, scalar_multiplication(p, k-1, curve), curve))
