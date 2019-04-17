def isgenerator(alpha, n, n_primes):
    identity = alpha ** 0

    for p in n_primes:
        power = alpha ** (n // p)

        if power == identity:
            return False

    return True
