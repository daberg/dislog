def pohlighellman(alpha, beta, n, n_factors):
    remainders = []
    moduli = []

    for p, e in n_factors.items():
        base = alpha ** (n // p)

        arg_base = beta
        cur_pow = 0
        next_pow = 1
        l = 0
        rem = 0

        for j in range(e):
            prev_l = l

            prev_pow = cur_pow
            cur_pow = next_pow
            next_pow *= p

            arg_base *= alpha ** (- prev_l * prev_pow)
            arg_exp = n // next_pow
            arg = arg_base ** arg_exp

            l = exhaustive(base, arg, n)

            if l is None:
                return None

            rem += l * cur_pow

        remainders.append(rem)
        moduli.append(p ** e)

    return crt(moduli, remainders)
