import dislog
import unittest


class ExhaustiveTestCase(unittest.TestCase):
    def test_exhaustive_modulo_integer(self):
        alfa = dislog.ModuloInteger(5, 97)
        beta = dislog.ModuloInteger(35, 97)
        n = 96

        self.assertEqual(
            dislog.exhaustive(alfa, beta, n),
            32,
            "Incorrect return value"
        )


if __name__ == '__main__':
    unittest.main()
