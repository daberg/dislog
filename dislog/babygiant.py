import math
from dislog.debug import debug


def babygiant(alfa, beta, n):
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
        exp_table[power] = j
        debug(babygiant, "Adding {} : {} to table", power, j)
        print(power, exp_table[power])

    # At each step, candidate equals beta * (alfa ^ m)^i
    factor = alfa ** -m
    candidate = beta
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
