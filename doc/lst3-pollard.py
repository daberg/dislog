_A_MAP = [
    lambda a, n: a,
    lambda a, n: (a * 2) % n,
    lambda a, n: (a + 1) % n
]

_B_MAP = [
    lambda b, n: (b + 1) % n,
    lambda b, n: (b * 2) % n,
    lambda b, n: b
]

_F_MAP = [
    lambda gamma, alpha, beta: gamma * beta,
    lambda gamma, alpha, beta: gamma ** 2,
    lambda gamma, alpha, beta: gamma * alpha
]

def _map(a, b, gamma, alpha, beta, n, s_num):
    a = _A_MAP[s_num](a, n)
    b = _B_MAP[s_num](b, n)
    gamma = _F_MAP[s_num](gamma, alpha, beta)
    return (a, b, gamma)

def pollard(alpha, beta, n, s_map, a_start=0, b_start=0):
    a_slow = a_fast = a_start
    b_slow = b_fast = b_start
    gamma_slow = gamma_fast = (alpha ** a_start) * (beta ** b_start)

    while True:
        a_slow, b_slow, gamma_slow = _map(
            a_slow, b_slow, gamma_slow, alpha, beta, n, s_map(gamma_slow)
        )

        for _ in range(2):
            a_fast, b_fast, gamma_fast = _map(
                a_fast, b_fast, gamma_fast, alpha, beta, n, s_map(gamma_fast)
            )

        if gamma_slow == gamma_fast:
            r = (b_slow - b_fast) % n

            if r == 0:
                return None

            r_inv = mod_inverse(r, n)

            if r_inv is None:
                return None

            return (r_inv * (a_fast - a_slow)) % n
