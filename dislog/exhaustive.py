from dislog.debug import debug


def exhaustive(alfa, beta, n):
    """Computes the discrete logarithm log_{alfa}(beta).

    Given a generator alfa of a cyclic group G, another element beta of the
    group G and the order n of the group G, computes the discrete logarithm
    of beta to the base of alpha.

    Args:
        alfa: logarithm base, must support internal equality and multiplication
            and integer exponentiation; should be a generator to guarantee the
            existence of the logarithm
        beta: logarithm argument, must support internal equality and
            multiplication
        n: order of the group containing alfa and beta

    Returns:
        The discrete logarithm log_{alfa}(beta) (the integer x such that alfa
        to the power of x equals beta) if it exists, None otherwise
    """
    # Current exponent and power value being evaluated
    exp = 0
    power = alfa ** 0

    debug("Alfa = {}, Beta = {}", alfa, beta)
    debug("Alfa^{} = {}", exp, power)

    while power != beta:
        exp = exp + 1

        # alfa is not a generator
        if exp == n:
            return None

        power = power * alfa

        debug("Alfa^{} = {}".format(exp, power))

    return exp
