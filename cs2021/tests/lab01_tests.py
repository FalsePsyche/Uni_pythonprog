# todo add unit tests here so vscode can use its built in python test system

from ../lab1/lab01.py import lab01.py

def _test():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    _test()
    lab01.factors(20)
