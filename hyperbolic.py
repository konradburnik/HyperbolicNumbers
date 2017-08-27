"""

   An implementation of hyperbolic complex numbers. A hyperbolic number is of
   the form a + bj where j**2 = +1.

   Copyright (c) Konrad Burnik, August 2017

"""
from math import sqrt

class HyperbolicNumber:
    """Represents a hyperbolic number a + bj where j**2 = +1."""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = HyperbolicNumber(other, 0)
        a = self.a + other.a
        b = self.b + other.b
        return HyperbolicNumber(a, b)

    def __radd__(self, other):
        if not (isinstance(other, int) or isinstance(other, float)):
            raise ValueError("Argument of wrong type, should be of type int or float!")
        return HyperbolicNumber(other + self.a, other + self.b)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = HyperbolicNumber(other, 0)
        a = self.a * other.a + self.b * other.b
        b = self.a * other.b + self.b * other.a
        return HyperbolicNumber(a, b)

    def __rmul__(self, other):
        if not (isinstance(other, int) or isinstance(other, float)):
            raise ValueError("Argument of wrong type, should be of type int or float!")
        return HyperbolicNumber(other.__mul__(self.a), other.__mul__(self.b))

    def __pow__(self, other):
        if not (isinstance(other, int)):
            raise ValueError("Argument of wrong type, should be of type int!")

        n = other
        num = HyperbolicNumber(self.a, self.b)

        if n < 0:
            raise ValueError("Number can only be raised by non-negative power!")
        if n == 0:
            return num
        # Exponentiation by squaring https://en.wikipedia.org/wiki/Exponentiation_by_squaring
        result = 1
        while n > 1:
            if n % 2 == 0:
                num = num * num
                n = n // 2
            else:
                result = num * result
                num = num * num
                n = (n - 1) // 2
        return num * result

    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = HyperbolicNumber(other, 0)
        return self.a == other.a and self.b == other.b

    def __repr__(self):
        return "({}, {})".format(self.a, self.b)

    def __str__(self):
        return "({}, {})".format(self.a, self.b)

    def __hash__(self):
        return hash((self.a, self.b))

def re(h):
    """Real part of hyperbolic number."""
    return h.a

def hyp(h):
    """Hyperbolic (or imaginary) part of hyperbolic number."""
    return h.b

def mag(h):
    """Returns the magnitude of a hyperbolic number."""
    return sqrt(re(h)**2 + hyp(h)**2)

if __name__ == "__main__":
    assert HyperbolicNumber(1, 2) + HyperbolicNumber(3, 4) == HyperbolicNumber(4, 6)
