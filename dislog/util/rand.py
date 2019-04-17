import random
import dislog as dg
import dislog.util as dgutil
from sympy.core.numbers import igcd as gcd
from sympy.ntheory import factorint
from sympy.ntheory import totient
from sympy.ntheory.primetest import isprime


def rand_cyclic_zstar(min_modulus, max_modulus):
    if min_modulus < 2 or max_modulus < min_modulus:
        raise ValueError("Must be: 2 <= min_modulus <= max_modulus")

    moduli = list(range(min_modulus, max_modulus + 1))
    random.shuffle(moduli)

    while moduli:
        modulus = moduli.pop()

        n = totient(modulus)
        n_primes = factorint(n).keys()

        elements = [i for i in range(modulus) if gcd(i, modulus) == 1]
        random.shuffle(elements)

        while elements:
            g = elements.pop()

            if dgutil.isgenerator(dg.ModuloInteger(g, modulus), n, n_primes):
                dgutil.debug(
                    rand_cyclic_zstar,
                    "Found Z_{} (order {}, generator {})", modulus, n, g
                )
                return (modulus, n, g)

    dgutil.debug(
        rand_cyclic_zstar,
        "No cyclic Z* found in the specified interval"
    )
    return None

def rand_zstar_element(modulus):
    candidates = list(range(1, modulus))
    random.shuffle(candidates)

    for candidate in candidates:
        if gcd(candidate, modulus) == 1:
            return candidate
    return None
