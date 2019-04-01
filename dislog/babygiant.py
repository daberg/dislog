import math
from dislog.debug import debug


def babygiant(alfa, beta, n):
    """Computes discrete logarithm using baby-step giant-step algorithm.

    Given a generator alfa of a cyclic group G, another element beta of the
    group G and the order n of the group G, computes the discrete logarithm
    of beta to the base of alpha using the baby-step giant-step algorithm.

    Args:
        alfa: logarithm base, must support internal equality and
            multiplication, integer exponentiation and hashing; should be a
            generator to guarantee the existence of the logarithm
        beta: logarithm argument, must support internal equality and
            multiplication
        n: order of the group containing alfa and beta

    Returns:
        The discrete logarithm log_{alfa}(beta) (the integer x such that alfa
        to the power of x equals beta) if it exists, None otherwise
    """
    m = math.ceil(math.sqrt(n))

    debug(babygiant, "alfa={}\tbeta={}\tn={}\tm={}", alfa, beta, n, m)

    # Exponent lookup table
    # Key: a^j, value: j
    exp_table = {}

    # Fill table (using multiplications for efficiency)
    power = alfa ** 0
    exp_table[power] = 0
    for j in range(1, m):
        power = power * alfa
        if power not in exp_table:
            exp_table[power] = j
        debug(babygiant, "Adding {} : {} to table", power, j)

    factor = alfa ** (-m) # Candidate is multiplied by it at every iteration
    if factor is None:
        debug(babygiant, "alfa^-m does not exist, cannot use babygiant")
        return None

    candidate = beta # Equals beta * (alfa ^ m)^i at each iteration
    for i in range(m):
        debug(babygiant, "Checking presence of {} in lookup table", candidate)
        if candidate in exp_table:
            exp = i * m + exp_table[candidate]
            debug(babygiant, "Found candidate; logarithm = {}", exp)
            return exp

        debug(babygiant, "Candidate not found; multiplying by {}", factor)
        candidate = candidate * factor

    debug(babygiant, "Logarithm does not exist")
    return None
