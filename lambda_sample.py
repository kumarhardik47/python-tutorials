import os


func = lambda x:x**x

print func(8)

nums = [1,2,3,4,5,6,7,8,9,10,12,14,16,19]

#for num in nums:
#	print num, ":", even(num)

even = filter(lambda e:(e%2==0),nums)  # return result
print even

odd = map(lambda e:(e%3 ==0),nums)  #map --> do the operation and return True or False
print odd

sqr = filter(lambda e:(e*2),nums) #filter --> return the result
print sqr
