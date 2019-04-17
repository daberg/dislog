"""
Python module implementing discrete logarithm algorithms for study purposes.

Usage example:

    import dislog


    # Initialize alpha (5) and beta (35) belonging to the multiplicative group
    # of integers Z_{97}, of order 96, for which alpha is a generator
    alpha = dislog.ModuloInteger(5, 97)
    beta = dislog.ModuloInteger(35, 97)
    n = 96

    # Compute the discrete logarithm of beta to the base alpha with an
    # exhaustive search
    dislog.exhaustive(alpha, beta, n)
"""

__all__ = [
    'babygiant', 'exhaustive', 'ModuloInteger', 'pohlighellman',
    'expollard', 'modint_pollard_map', 'pollard'
]


from dislog.babygiant import babygiant
from dislog.exhaustive import exhaustive
from dislog.modulointeger import ModuloInteger
from dislog.pohlighellman import pohlighellman
from dislog.pollard import expollard
from dislog.pollard import modint_pollard_map
from dislog.pollard import pollard
