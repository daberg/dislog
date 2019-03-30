import dislog
import unittest


class DislogTestCase(unittest.TestCase):
    def test_modulo_integer(self):
        # Entry structure: (alfa, beta, modulus, expected value)
        cases = [
            (5, 35, 97, 32)
        ]

        for case in cases:
            alfa = dislog.ModuloInteger(case[0], case[2])
            beta = dislog.ModuloInteger(case[1], case[2])
            n = case[2] - 1
            expected_value = case[3]

            self.assertEqual(
                dislog.exhaustive(alfa, beta, n),
                expected_value,
                "Incorrect return value for exhaustive algorithm"
            )

            self.assertEqual(
                dislog.babygiant(alfa, beta, n),
                expected_value,
                "Incorrect return value for baby-step giant-step algorithm"
            )

if __name__ == '__main__':
    unittest.main()
