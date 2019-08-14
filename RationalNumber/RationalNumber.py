import math


class RationalNumber:
    """
    Rational numbers class.
    """

    def __init__(self, a, b):
        self.a, self.b = self.__normalize__(a, b)

    def __add__(self, other):
        new_a, new_b = self.a * other.b + self.b * other.a, self.b * other.b
        return RationalNumber(new_a, new_b)

    def __radd__(self, other):
        if isinstance(other, int):
            return self + RationalNumber(other, 1)

    def __sub__(self, other):
        new_a, new_b = self.a * other.b - self.b * other.a, self.b * other.b
        return RationalNumber(new_a, new_b)

    def __mul__(self, other):
        return RationalNumber(self.a * other.a, self.b * other.b)

    def __truediv__(self, other):
        return RationalNumber(self.a * other.b, self.b * other.a)

    def __str__(self):
        return f"{self.a}/{self.b}"

    @staticmethod
    def __normalize__(x, y):
        gcd = math.gcd(x, y)
        x = x // gcd
        y = y // gcd
        return x, y


if __name__ == "__main__":
    a = RationalNumber(1, 3)
    b = RationalNumber(5, 6)

    print(2 + a)  # just for fun
    print(a, b)
    print(a + b)
    print(a - b)
    print(a / b)
