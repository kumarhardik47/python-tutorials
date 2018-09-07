import os
import copy

x = {'a':1,'b':2}
y = {'b':5,'c':6}
print x,y
#z = {**x, **y} for 3.4 and higher

z = copy.deepcopy(x)
z.update(y)

print z
print x,y
