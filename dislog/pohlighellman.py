import dislog
from dislog.util import debug


def pohlighellman(alfa, beta, n, n_factors):
    """Computes discrete logarithm using Pohlig-Hellman algorithm.

    Given a generator alfa of a cyclic group G, another element beta of the
    group G and the order n of the group G, computes the discrete logarithm
    of beta to the base of alpha using the Pohlig-Hellman algorithm.

    Args:
        alfa: logarithm base, must support internal equality and
            multiplication and integer exponentiation; should be a generator to
            guarantee the existence of the logarithm
        beta: logarithm argument, must support internal equality and
            multiplication
        n: order of the group containing alfa and beta
        n_factors: dictionary containing the factors of n as keys and their
            multiplicity as values

    Returns:
        The discrete logarithm log_{alfa}(beta) (the integer x such that alfa
        to the power of x equals beta) if it exists, None otherwise
    """
    X = []

    for q, e in n_factors.items():
        base = alfa ** (n // q)

        arg_base = beta
        l = 0
        new_x = 0

        # prev_l ?

        for j in range(e - 1):
            arg_base = arg_base * (alpha ** l)
            arg_exp = n // (q ^ (j + 1))
            arg = arg_base ** arg_exp

            l = dislog.exhaustive(base, arg)

            new_x =
