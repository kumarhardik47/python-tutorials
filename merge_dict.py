import os


x = {'a':1,'b':2}
y = {'b':5,'c':6}

#z = {**x, **y} for 3.4 and higher

z = x.copy()
z.update(y)
print z
