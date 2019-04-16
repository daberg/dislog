def exhaustive(alpha, beta, n):
    exp = 0
    power = alpha ** 0

    while power != beta:
        exp += 1

        if exp == n:
            return None

        power *= alpha

    return exp
