#input 
# n = number of items e.g 5)
#1 2 3 4 5

#2+3+4+5=14
#1+3+4+5=13
#1+2+4+5=12
#1+2+3+5=11
#1+2+3+4=10
#mix, max = 10,14 outout

import os

n  = int(raw_input("Enter the total count of numbers"))

print ('Enter %s numbers' % n)
l = []
for i in range(n):
	l.append(int(raw_input()))

min_sum = 0
max_sum = 0

m  = sorted(l)

#min_sum
for i in m[0:n-1]:
	min_sum+=i
#max_sum
for i in m[1:n]:
	max_sum+=i
print min_sum,max_sum


