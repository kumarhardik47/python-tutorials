import os

a = [22,23,34]
b=[45,56,78]

#filter expects two arguments. so map is suitable here
maptest = map(lambda x,y:x>y, a,b)
print maptest

c = map(lambda x,y:x+y, a,b)
print c

d =   map(lambda x:x**2,[2,4,6,8])
print d


print map(pow,[2,4,6],[5,6,2])



print filter((lambda x:x>22), a)
print filter((lambda x:x>19), range(20,30))

l1 = [1,2,3,4,5,6,7]
l2 = [2,4,5,6,9,10]

print filter(lambda x:x in l1,l2)
#OR
print list(x for x in l1 if x in l2) #List Comprehension


print reduce(lambda x,y:x*y,l1) # -->  ((((((1*2)*3)*4)*5)*6)*7)

L = ['Testing ', 'shows ', 'the ', 'presence', ', ','not ', 'the ', 'absence ', 'of ', 'bugs']
print ''.join(L)

print type(l1)
print ''.join(l1)# this will fail because join expects string and list passed

