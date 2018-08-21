import re

text = "aaadaa"
new = "aa"
pattern = re.compile(new)

r = pattern.search(text)

print r.group()
while r:	
    print "({0}, {1})".format(r.start(), r.end()-1)
    r = pattern.search(text,r.start()+1 )
