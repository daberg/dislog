import dislog
from dislog.util import debug
from sympy.ntheory.modular import crt


def pohlighellman(alpha, beta, n, n_factors):
    """Computes discrete logarithm using Pohlig-Hellman algorithm.

    Given a generator alpha of a cyclic group G, another element beta of the
    group G, the order n of the group G and the prime factorization of n,
    computes the discrete logarithm of beta to the base of alpha using the
    Pohlig-Hellman algorithm.

    Args:
        alpha: logarithm base, must support internal equality and
            multiplication and integer exponentiation; should be a generator to
            guarantee the existence of the logarithm
        beta: logarithm argument, must support internal equality and
            multiplication
        n: order of the group containing alpha and beta
        n_factors: dictionary containing the prime factors of n as keys and
            their multiplicity as values

    Returns:
        The discrete logarithm log_{alpha}(beta) (the integer x such that alpha
        to the power of x equals beta) if it exists, None otherwise
    """
    debug(
        pohlighellman,
        "alpha={} beta={} n={} factors={}", alpha, beta, n, n_factors
    )

    # List of remainder values and moduli to be solved with C.r.t.
    remainders = []
    moduli = []

    # For each factor p, store x mod (p ^ e) together with the modulus
    for p, e in n_factors.items():
        debug(pohlighellman, "Factor: {}^{}", p, e)

        # Initialize reduced logarithm base, constant
        base = alpha ** (n // p)

        # Initialize helper variables
        arg_base = beta
        cur_pow = 0
        next_pow = 1
        l = 0
        rem = 0

        # Compute expansion coefficients
        for j in range(e):
            debug(pohlighellman, "Calculating l_({})", j)

            prev_l = l  # l_{j - 1}

            prev_pow = cur_pow       # p ^ (j - 1) for j > 0
            cur_pow = next_pow       # p ^ (j)
            next_pow *= p            # p ^ (j + 1)

            arg_base *= alpha ** (- prev_l * prev_pow)
            arg_exp = n // next_pow
            arg = arg_base ** arg_exp

            l = dislog.exhaustive(base, arg, n)

            if l is None:
                debug(pohlighellman, "Could not calculate reduced logarithm")
                return None
            debug(pohlighellman, "l_({})={}", j, l)

            rem += l * cur_pow

        debug(pohlighellman, "Found congruence: x = {} mod ({}^{})", rem, p, e)

        remainders.append(rem)
        moduli.append(p ** e)

    debug(pohlighellman, "Applying Chinese remainder theorem")
    ret = crt(moduli, remainders)

    if ret is not None:
        ret = ret[0]
        debug(pohlighellman, "Logarithm={}", ret)
    else:
        debug(pohlighellman, "No solution found")

    return int(ret)
