import decimal
import math
from dislog.util import debug

def _round_sqrt(n):
    # Conversion to handle decimal operations on big numbers
    dec_n = decimal.Decimal(n)

    # Set precision for calculating the square root of n up to at least one
    # digit beyond the decimal point
    num_digits = dec_n.adjusted() + 1
    prec = num_digits // 2 + 2
    context = decimal.Context(prec=prec, rounding=decimal.ROUND_UP)

    # Find root of order and round it up
    dec_sqrt = dec_n.sqrt(context)
    sqrt = int(dec_sqrt.to_integral_value(context=context))
    debug(_round_sqrt, "sqrt={} rounded_sqrt={}", dec_sqrt, sqrt)

    return sqrt

def babygiant(alpha, beta, n, m=None):
    """Computes discrete logarithm using baby-step giant-step algorithm.

    Given a generator alpha of a cyclic group G, another element beta of the
    group G and the order n of the group G, computes the discrete logarithm
    of beta to the base of alpha using the baby-step giant-step algorithm.

    Args:
        alpha: logarithm base, must support internal equality and
            multiplication, integer exponentiation and hashing; should be a
            generator to guarantee the existence of the logarithm
        beta: logarithm argument, must support internal equality and
            multiplication
        n: order of the group containing alpha and beta
        m: number of elements that the algorithm can store in memory; should be
            less than n; if not specified, it is set to ceil(sqrt(n))

    Returns:
        The discrete logarithm log_{alpha}(beta) (the integer x such that alpha
        to the power of x equals beta) if it exists, None otherwise
    """
    debug(babygiant, "alpha={}\tbeta={}\tn={}\t", alpha, beta, n)

    if m is None:
        m = _round_sqrt(n)

    # Exponent lookup table
    # Key: a^j, value: j
    exp_table = {}

    # Fill table (using multiplications for efficiency)
    power = alpha ** 0
    exp_table[power] = 0
    for j in range(1, m):
        power *= alpha
        if power not in exp_table:
            exp_table[power] = j
        debug(babygiant, "Adding {} : {} to table", power, j)

    factor = alpha ** (-m)
    if factor is None:
        debug(babygiant, "alpha^-m does not exist, cannot use babygiant")
        return None

    # At each iteration, candidate = beta * ((alpha ^ -m) ^ i)
    candidate = beta

    # Check all powers up to the ceil of n / m not included
    for i in range((n + m - 1) // m):
        debug(babygiant, "Checking presence of {} in lookup table", candidate)
        if candidate in exp_table:
            exp = i * m + exp_table[candidate]
            debug(babygiant, "Found candidate; logarithm = {}", exp)
            return exp

        debug(babygiant, "Candidate not found; multiplying by {}", factor)
        candidate *= factor

    debug(babygiant, "Logarithm does not exist")
    return None
