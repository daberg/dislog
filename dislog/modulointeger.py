from numbers import Number


class ModuloInteger:
    def __init__(self, value, modulus):
        if not isinstance(value, Number):
            raise TypeError("Value must be initialized with a number")

        if not isinstance(modulus, Number):
            raise TypeError("Modulus must be initialized with a number")

        if (modulus != int(modulus)
            or modulus < 1):
            raise ValueError(
                "Modulus must be initialized with an integer greater than 0"
            )

        self.modulus = int(modulus)
        self.value = int(value) % self.modulus

    def __eq__(self, other):
        if isinstance(other, ModuloInteger):
            return self.value == other.value
        return False

    def __mul__(self, other):
        if not isinstance(other, ModuloInteger):
            raise TypeError("Trying to multiply by a non-ModuloInteger object")

        if self.modulus != other.modulus:
            raise ValueError("Modulus must be the same")

        mul = (self.value * other.value) % self.modulus
        return ModuloInteger(mul, self.modulus)

    def __pow__(self, exponent):
        if not isinstance(exponent, int):
            raise TypeError("Exponent must be an integer")

        if exponent == 0:
            newvalue = 1
        else:
            # Could be optimized memory-wise
            newvalue = (self.value ** abs(exponent)) % self.modulus

        if exponent < 0:
            return ModuloInteger(newvalue, self.modulus).inverse()

        return ModuloInteger(newvalue, self.modulus)

    def __str__(self):
        return "{} (mod {})".format(self.value, self.modulus)
