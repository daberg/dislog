import dislog
import unittest


class ModuloIntegerTestCase(unittest.TestCase):
    def test_modulointeger_inverse(self):
        # Case list entry struture: (value, modulus, expected_inverse_value)
        cases = [
            (1, 3, 1),
            (2, 3, 2),
            (2, 6, None),
            (4, 9, 7),
            (67, 119, 16)
        ]

        for case in cases:
            value = case[0]
            modulus = case[1]
            expected_inverse_value = case[2]

            modulo_integer = dislog.ModuloInteger(value, modulus)
            inverse = modulo_integer.inverse()
            inverse_value = inverse.value if inverse else None

            self.assertEqual(
                inverse_value,
                case[2],
                "Incorrect inverse return value for {}".format(modulo_integer)
            )

            if expected_inverse_value:
                self.assertEqual(
                    (modulo_integer * inverse),
                    dislog.ModuloInteger(1, modulus),
                    "Multiplication result should be 1"
                )


if __name__ == '__main__':
    unittest.main()
