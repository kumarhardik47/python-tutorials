import os


def my_gen(num):
	for i in range(num):
		yield i

r = my_gen(10)


print r.next()
print r.next()
print r.next()
print r.next()
print r.next()
print r.next()
print r.next()
print r.next()
print r.next()
print r.next()
print r.next()
print r.next()
