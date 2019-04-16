def exhaustive(alpha, beta, n):
    exp = 0
    power = alpha ** 0

    while power != beta:
        exp = exp + 1

        if exp == n:
            return None

        power = power * alpha

    return exp
