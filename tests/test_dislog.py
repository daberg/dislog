import dislog
import unittest
from sympy.ntheory import factorint


class DislogTestCase(unittest.TestCase):
    def test_modulo_integer(self):
        # Entry structure: (alpha, beta, modulus, n, expected value)
        cases = [
            (2, 1, 3, 2, 0),
            (33, 47, 50, 20, 19),
            (897, 654, 1709, 1708, None)
        ]

        for case in cases:
            alpha = dislog.ModuloInteger(case[0], case[2])
            beta = dislog.ModuloInteger(case[1], case[2])
            n = case[3]
            expected_value = case[4]

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
                "Incorrect return value for Pohlig-Hellman algorithm"
            )

            self.assertEqual(
                dislog.pollard(alpha, beta, n, dislog.modint_pollard_map),
                expected_value,
                "Incorrect return value for Pollard algorithm"
            )

if __name__ == '__main__':
    unittest.main()
