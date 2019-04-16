def babygiant(alpha, beta, n):
    dec_n = decimal.Decimal(n)
    num_digits = dec_n.adjusted() + 1
    prec = num_digits // 2 + 2
    context = decimal.Context(prec=prec, rounding=decimal.ROUND_UP)

    dec_m = dec_n.sqrt(context)
    m = int(dec_m.to_integral_value(context=context))

    exp_table = {}

    power = alpha ** 0
    exp_table[power] = 0
    for j in range(1, m):
        power = power * alpha
        if power not in exp_table:
            exp_table[power] = j

    factor = alpha ** (-m)
    if factor is None:
        return None

    candidate = beta
    for i in range(m):
        if candidate in exp_table:
            exp = i * m + exp_table[candidate]
            return exp

        candidate = candidate * factor

    return None
