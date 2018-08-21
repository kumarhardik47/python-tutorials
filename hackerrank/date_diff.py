import os

x1 = "Sun 10 May 2015 13:54:36 -0700"
x2 = "Sun 10 May 2015 13:54:36 -0000"
x3 = "Sat 02 May 2015 19:54:36 +0530"
x4 = "Fri 01 May 2015 13:54:36 -0000"
(x1,x2) = re.findall('(^.*) ([+-]\d{4})',s)[0]
tz = x2[0] + str(int(x2[1:3])*3600 + int(x2[3:5])*60)
ts = time.strptime(x1,"%a %d %b %Y %H:%M:%S")
print (time.mktime(ts) - eval(tz))
