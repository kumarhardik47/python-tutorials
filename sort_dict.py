import os
import json
mydict = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}

a = {}
for key in sorted(mydict.iterkeys()):
    #b = {key:mydict[key]}
    print key
    #a.update("%s:%s" % (key, mydict[key]))
    #a.update(b)
#print a
#d = json.loads(a)
#print d
