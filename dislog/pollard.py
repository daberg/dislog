from dislog import ModuloInteger
from dislog.util import debug
from sympy.core.numbers import mod_inverse
from sympy.ntheory.primetest import isprime


# _map helper list for alfa exponents
_A_MAP = [
    lambda a, n: a,
    lambda a, n: (a * 2) % n,
    lambda a, n: (a + 1) % n
]

# _map helper list for beta exponents
_B_MAP = [
    lambda b, n: (b + 1) % n,
    lambda b, n: (b * 2) % n,
    lambda b, n: b
]

# _map helper list for group elements
_X_MAP = [
    lambda x, alpha, beta: x * beta,
    lambda x, alpha, beta: x ** 2,
    lambda x, alpha, beta: x * alpha
]

# Maps a triple (alpha exponent, beta exponent, group element) to the next one,
# according to the subset number of the group element
def _map(a, b, x, alpha, beta, n, s_num):
    debug(
        pollard,
        "Calculating _map for: s_num={} a={} b={} x={} n={}", s_num, a, b, x, n
    )
    a = _A_MAP[s_num](a, n)
    b = _B_MAP[s_num](b, n)
    x = _X_MAP[s_num](x, alpha, beta)
    return (a, b, x)

def pollard(alpha, beta, n, s_map, a_start=0, b_start=0):
    """Computes discrete logarithm using Pollard's Rho algorithm.

    Given a generator alpha of a cyclic group G, another element beta of G,
    the order n of G and a suitable partitioning function on G, computes the
    discrete logarithm of beta to the base of alpha using Pollard's algorithm.

    Args:
        alpha: logarithm base, must support internal equality and
            multiplication and integer exponentiation; should be a generator to
            guarantee the existence of the logarithm
        beta: logarithm argument, must support internal equality and
            multiplication and integer exponentiation
        n: order of the group containing alpha and beta
        s_map: function mapping group elements to their partition; must returns
            an integer between 0 and 2 representing the partition number
        a_start: starting coefficient in the sequence of the alpha exponents
        b_start: starting coefficient in the sequence of the beta exponents

    Returns:
        The discrete logarithm log_{alpha}(beta) (the integer x such that alpha
        to the power of x equals beta) if it exists and it finds it given the
        starting parameters, None otherwise
    """
    debug(pollard, "alpha={} beta={} n={}", alpha, beta, n)
    debug(pollard, "s_map={} a_start={} b_start={}", s_map, a_start, b_start)

    # Initialization
    a_slow = a_fast = a_start
    b_slow = b_fast = b_start
    x_slow = x_fast = (alpha ** a_start) * (beta ** b_start)

    debug(pollard, "a={} b={} x={}", a_slow, b_slow, x_slow)
    debug(pollard, "A={} B={} X={}", a_fast, b_fast, x_fast)

    while True:
        debug(pollard, "Increasing")

        # Floyd's tortoise increase
        a_slow, b_slow, x_slow = _map(
            a_slow, b_slow, x_slow,
            alpha, beta, n, s_map(x_slow)
        )
        debug(pollard, "a={} b={} x={}", a_slow, b_slow, x_slow)
        assert((alpha ** a_slow) * (beta ** b_slow) == x_slow)

        # Floyd's hare double increase
        for _ in range(2):
            a_fast, b_fast, x_fast = _map(
                a_fast, b_fast, x_fast,
                alpha, beta, n, s_map(x_fast)
            )
            debug(pollard, "A={} B={} X={}", a_fast, b_fast, x_fast)
            assert((alpha ** a_fast) * (beta ** b_fast) == x_fast)

        # Found loop
        if x_slow == x_fast:
            debug(pollard, "Found loop: x={} X={}", x_slow, x_fast)
            debug(pollard, "            a={} A={}", a_slow, a_fast)
            debug(pollard, "            b={} B={}", b_slow, b_fast)

            assert(
                (alpha ** a_slow) * (beta ** b_slow) ==
                (alpha ** a_fast) * (beta ** b_fast)
            )

            r = (b_slow - b_fast) % n

            debug(pollard, "(b - B) mod n = {}", r)

            if r == 0:
                return None

            try:
                r_inv = mod_inverse(r, n)

            except ValueError:
                debug(pollard, "Failure: r={} not invertible", r)
                return None

            debug(pollard, "r_inv={}", r_inv)

            log = (r_inv * (a_fast - a_slow)) % n
            debug(pollard, "Returning logarithm={}", log)

            return log

def expollard(alpha, beta, n, s_map):
    debug(expollard, "alpha={} beta={} n={} s_map={}", alpha, beta, n, s_map)
    for a_start in range(n):
        for b_start in range(n):
            ret = pollard(alpha, beta, n, s_map, a_start, b_start)
            if ret is not None:
                return ret
    debug(expollard, "No suitable starting values were found")
    return None


# modint_pollard_map helper list
_MODINT_MAP = [1, 0, 2]

# Subset map for ModuloInteger instances
def modint_pollard_map(modulo_integer_x):
    return _MODINT_MAP[modulo_integer_x.value % 3]
