import os


def printf(string, *formatargs):
    print(string.format(*formatargs))

def dummy(*args):
    pass


debug = printf if "DISLOGDEBUG" in os.environ else dummy
