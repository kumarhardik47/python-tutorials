import re

text = "aaadaa"
new = "aa"
pattern = re.compile(new)

r = pattern.search(text)

#print r.group()
print  text, new
while r:	
    print "({0}, {1})".format(r.start(), r.end()-1)
    r = pattern.search(text,r.start()+1)



out = re.finditer(r'aa',text)
if out:
	for o in out:
		print text[o.start():o.end()], "start:",o.start(), "end:", o.end()
else:
	print "No pattern found"
