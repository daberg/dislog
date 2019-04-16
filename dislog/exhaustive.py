from dislog.util import debug


def exhaustive(alpha, beta, n):
    """Computes discrete logarithm with a naive exhaustive approach.

    Given a generator alpha of a cyclic group G, another element beta of the
    group G and the order n of the group G, computes the discrete logarithm
    of beta to the base of alpha with an exhaustive approach.

    Args:
        alpha: logarithm base, must support internal equality and multiplication
            and integer exponentiation; should be a generator to guarantee the
            existence of the logarithm
        beta: logarithm argument, must support internal equality and
            multiplication
        n: order of the group containing alpha and beta

    Returns:
        The discrete logarithm log_{alpha}(beta) (the integer x such that alpha
        to the power of x equals beta) if it exists, None otherwise
    """
    debug(exhaustive, "alpha={}, beta={}, n={}", alpha, beta, n)

    # Current exponent and power value being evaluated
    exp = 0
    power = alpha ** 0

    debug(exhaustive, "alpha^{}={}", exp, power)

    while power != beta:
        exp += 1

        # alpha is not a generator
        if exp == n:
            debug(exhaustive, "n={} reached; logarithm does not exist", n)
            return None

        power *= alpha
        debug(exhaustive, "alpha^{} = {}".format(exp, power))

    debug(exhaustive, "Logarithm = {}", exp)
    return exp
