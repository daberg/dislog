import os


def debugprint(function, message, *formatargs):
    print(
        "[{}:{}]\t".format(function.__module__, function.__name__)
        + message.format(*formatargs)
    )

def dummy(*args):
    pass


debug = debugprint if "DISLOGDEBUG" in os.environ else dummy
