import os
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

test = ""
for c in reverse('abcdef'):
	test+=c

print test


