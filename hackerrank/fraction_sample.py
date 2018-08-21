from __future__ import print_function
from fractions import Fraction
import os


def product(fracs):
    #t = # complete this line with a reduce statement
    #return t.numerator, t.denominator
    pass


if __name__ == '__main__':
    fracs = []
    for _ in range(input()):
        fracs.append(Fraction(*map(int, raw_input().split())))
    print fracs
    result = product(fracs)
    print(*result)
