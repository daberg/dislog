from dislog.debug import debug
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

    def inverse(self):
        """Computes the ModuloInteger inverse of the instance.

        With a and n respectively value and modulus of the ModuloInteger
        instance, finds the value x s.t. ax = 1 mod n.

        It does that by solving the equivalent diophantine equation
        ax + ny = 1, using an adapted version of the extended euclidean
        algorithm.

        It can be proved that a solution exists iff gcd(a,n) = 1, that is iff a
        is coprime to n.

        In particular, x is found as the left coefficient of Bézout's identity:
        ax + ny = gcd(a,n).

        Args:
            self: the ModuloInteger instance of which the inverse has to be
                computed

        Returns:
            A ModuloInteger representing the inverse if it exists, None
            otherwise
        """
        # Initialized with n and a respectively
        r = self.modulus
        r_new = self.value

        x = 0
        x_new = 1

        debug("[ModuloInteger] Inverse of {}".format(self))
        debug(
            "[ModuloInteger]\t\tr={}\tr_new={}\tx={}\tx_new={}"
            .format(r, r_new, x, x_new)
        )

        # Finds r = gcd(a,n) and left solution x
        while r_new != 0:
            quotient = r // r_new
            r, r_new = r_new, r - quotient * r_new
            x, x_new = x_new, x - quotient * x_new

            debug(
                "[ModuloInteger]\tq={}\tr={}\tr_new={}\tx={}\tx_new={}"
                .format(quotient, r, r_new, x, x_new)
            )

        # No solution exists, since gcd(a, n) != 1 (a and n are not coprime)
        if r > 1:
            return None

        # Left solutions are of the form: x + kn.
        # For only two of them, abs(x) < n: these are called minimal
        # solutions. One will be x* and the other -x*, with 0 < x* < n.
        # Extended GCD finds either one or the other.
        # If it finds the negative one, n must be added to make it positive.
        if x < 0:
            debug("[ModuloInteger] Adding {} to x".format(self.modulus))
            x = x + self.modulus

        return ModuloInteger(x, self.modulus)
