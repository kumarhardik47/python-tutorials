import os

def subsets(s):
    for cardinality in range(len(s) + 1):
        yield from combinations(s, cardinality)


print subsets([1,2,3,4,5])
