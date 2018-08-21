import re

count = int(raw_input())
for i in range(count):
    num = raw_input()
    r = re.match(r'\d[]', num)
    print r
    if r and len(num)== 10:
        print "YES"
    else:
        print "NO"
