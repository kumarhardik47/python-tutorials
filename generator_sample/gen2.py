#sample program for control flow of generators.

import os

def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

itr = my_gen()
#observe the outpput about the control flow for generators.
for i in itr:
	print i
	#pass if only pass then i will not be printed

