from math import *


class _complex:
    """
    Complex number class
    """

    def __init__(self, real, im):
        self.real = real
        self.im = im
        self.module = sqrt(self.real**2 + self.im**2)
        self.angle = atan(self.im / self.real)

    def _polar_to_rectangular(self, module, angle):
        return _complex(module * cos(angle), module * sin(angle))

    def __add__(self, other):
        return _complex(self.real + other.real, self.im + other.im)

    def __sub__(self, other):
        return _complex(self.real - other.real, self.im - other.im)

    def __mul__(self, other):
        return self._polar_to_rectangular(
            self.module * other.module, self.angle + other.angle
        )

    def __truediv__(self, other):
        return self._polar_to_rectangular(
            self.module / other.module, self.angle - other.angle
        )

    def __repr__(self):
        if self.im >= 0:
            return f"{self.real}+{self.im}j"
        else:
            return f"{self.real}{self.im}j"

    def __str__(self):
        return f"{self.real}+{self.im}j"

    def __eq__(self):
        pass  # TODO

    def __abs__(self):
        pass  # TODO

    def __eq__(self):
        pass  # TODO

    def __ge__(self):
        pass  # TODO

    def __gt__(self):
        pass  # TODO

    def __le__(self):
        pass  # TODO

    def __lt__(self):
        pass  # TODO

    def __ne__(self):
        pass  # TODO

    def __pow__(self):
        pass  # TODO

    def conjugate(self):
        pass  # TODO

    def imag(self):
        pass  # TODO

    def real(self):
        pass  # TODO

