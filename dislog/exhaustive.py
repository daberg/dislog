from dislog.debug import debug


def exhaustive(alfa, beta, n):
    """Computes discrete logarithm with a naive exhaustive approach.

    Given a generator alfa of a cyclic group G, another element beta of the
    group G and the order n of the group G, computes the discrete logarithm
    of beta to the base of alpha with an exhaustive approach.

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

    debug(exhaustive, "alfa = {}, beta = {}", alfa, beta)
    debug(exhaustive, "alfa^{} = {}", exp, power)

    while power != beta:
        exp = exp + 1

        # alfa is not a generator
        if exp == n:
            debug(exhaustive, "Logarithm does not exist")
            return None

        power = power * alfa
        debug(exhaustive, "alfa^{} = {}".format(exp, power))

    debug(exhaustive, "Logarithm = {}", exp)
    return exp
