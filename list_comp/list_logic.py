import os


l = [1,2,3,4,5]

print 1%2
print 2%2
print 3%2
print 4%2
print 5%2
print '*' * 80
print (x*2 for x in l if x%2)
print (x*2 for x in l if x%2==0)


itr =  (x*2 for x in l if x%2)

for i in itr:
	print i

print '*' * 80
itr =  (x*2 for x in l if x%2==0)

for i in itr:
	print i
