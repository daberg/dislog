"""
Python module implementing discrete logarithm algorithms for study purposes.

Usage example:

    import dislog


    # Initaliaze alfa (5) and beta (35) belonging to the multiplicative group
    # of integers Z_{97}, of order 96, for which alfa is a generator
    alfa = dislog.ModuloInteger(5, 97)
    beta = dislog.ModuloInteger(35, 97)
    n = 96

    # Compute the discrete logarithm log_{alfa}(beta) with an exhaustive search
    dislog.exhaustive(alfa, beta, n)
"""

__all__ = ['exhaustive', 'ModuloInteger']


from dislog.exhaustive import exhaustive
from dislog.modulointeger import ModuloInteger
