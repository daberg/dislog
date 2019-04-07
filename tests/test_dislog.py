import dislog
import unittest
from sympy.ntheory import factorint


class DislogTestCase(unittest.TestCase):
    def test_modulo_integer(self):
        # Entry structure: (alpha, beta, modulus, expected value)
        cases = [
            (2, 1, 3, 0),
            (5, 35, 97, 32),
            (71, 210, 251, 197),
            (897, 654, 1709, None)
        ]

        for case in cases:
            alpha = dislog.ModuloInteger(case[0], case[2])
            beta = dislog.ModuloInteger(case[1], case[2])
            n = case[2] - 1
            expected_value = case[3]

            self.assertEqual(
                dislog.exhaustive(alpha, beta, n),
                expected_value,
                "Incorrect return value for exhaustive algorithm"
            )

            self.assertEqual(
                dislog.babygiant(alpha, beta, n),
                expected_value,
                "Incorrect return value for baby-step giant-step algorithm"
            )

            self.assertEqual(
                dislog.pohlighellman(alpha, beta, n, factorint(n)),
                expected_value,
                "Incorrect return value for pohlig-hellman algorithm"
            )

if __name__ == '__main__':
    unittest.main()
