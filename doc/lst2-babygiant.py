def babygiant(alpha, beta, n, m=None):
    if m is None:
        m = round_sqrt(n)

    exp_table = {}

    power = alpha ** 0
    exp_table[power] = 0
    for j in range(1, m):
        power *= alpha
        if power not in exp_table:
            exp_table[power] = j

    factor = alpha ** (-m)
    if factor is None:
        return None

    candidate = beta
    for i in range((n + m - 1) // m):
        if candidate in exp_table:
            return i * m + exp_table[candidate]

        candidate *= factor

    return None
