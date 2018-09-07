import os
import json


#dumps --> (string or json) to (str)
#loads -->
#load would take a file-like object, read the data from that object, and use that string to create an object

#Note that dump and load convert between files and objects, while dumps and loads convert between strings and objects. You can think of the s-less functions as wrappers around the s functions:

s = "{a:1,b:2}"

#j = s.loads(s) # error string has no loads or laod

j = json.dumps(s) 
print j, type(j)

k =  json.loads(j) #load will fail 
print k, type(k)

j = json.dump(s) 
print j, type(j)

k =  json.load(j) #load will fail 
print k, type(k)
#l = json.dump(s) # error string has no dumps or dump
#print l, type(l)
#m = json.load(s) # error string has no dumps or dump
#print m, type(m)

s2 = {"a":1,"b":2}

k = json.dumps(s2) # 
print k, type(k)

