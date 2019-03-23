from dislog.debug import debug


def exhaustive(alfa, beta, p):
    """Computes the discrete logarithm log_{alfa}(beta) in Z*_{p}, that is the
    logarithm of beta to the base of alpha in the multiplicative group of the
    integers modulo p.

    Args:
        alfa: base of the logarithm, should be a generator of Z*_{p} to
              guarantee the existence of the logarithm
        beta: logarithm argument, must belong to Z*_{p}
        p: modulo of the integers

    Returns:
        The discrete logarithm log_{alfa}(beta) if it exists, None otherwise
    """
    # Order of the cyclic group
    n = p - 1

    # Current exponent and power value being evaluated
    exp = 0
    power = 1

    debug("Alfa = {}, Beta = {}, p = {}", alfa, beta, p)
    debug("Alfa^{} = {}", exp, power)

    while power != beta:
        exp = exp + 1

        # alfa is not a generator for Z*_{p}
        if exp == n:
            return None

        power = power * alfa % p

        debug("Alfa^{} = {}".format(exp, power))

    return exp
