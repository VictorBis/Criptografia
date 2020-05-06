from random import randint


class Participant():

    def __init__(self, p, g, participant):
        """
        Constructor de clase
        """
        self.p = p
        self.g = g
        self.participant = participant
        self.a = randint(0, self.p) % self.p

    def seed(self):
        """
        Generador de la parte propia del intercambio de Diffie-Hellmann
        """
        return pow(self.g, self.a, self.p)

    def exchange(self):
        """
        Adquiero el número de la otra persona y calculo mi propia llave.
        """
        n = self.participant.seed()
        return pow(n, self.a, self.p)
