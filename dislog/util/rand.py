import random
from dislog.util import debug
from fractions import gcd
from sympy.ntheory.primetest import isprime


def rand_mult_integer_generator(min_int, max_int):
    if min_int < 1 or max_int < min_int:
        raise ValueError("Must be: 1 <= min_int <= max_int")

    numbers = list(range(min_int, max_int + 1))
    random.shuffle(numbers)

    while numbers:
        p = numbers.pop()

        if not isprime(p):
            continue

        # Z*_{p + 1} has prime order p, hence any element execpt 1 will be a
        # generator
        modulus = p + 1
        candidates = list(range(2, modulus))
        random.shuffle(candidates)

        for candidate in candidates:
            if gcd(candidate, modulus) == 1:
                return (candidate, modulus)

    debug(rand_mult_integer_generator, "No primes found")
    return None

def rand_mult_integer(modulus):
    candidates = list(range(1, modulus))
    random.shuffle(candidates)

    for candidate in candidates:
        if gcd(candidate, modulus) == 1:
            return candidate
    return None
