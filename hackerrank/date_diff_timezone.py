import os
from dateutil import parser

x1 = "Sun 10 May 2015 13:54:36 -0700"
x2 = "Sun 10 May 2015 13:54:36 -0000"
x3 = "Sat 02 May 2015 19:54:36 +0530"
x4 = "Fri 01 May 2015 13:54:36 -0000"


d1 = parser.parse(x1.strip())
d2 = parser.parse(x2.strip())
print x1,"#############", d1
print x2,"##############",  d2
print(abs(int((d2-d1).total_seconds())))

d1 = parser.parse(x3.strip())
d2 = parser.parse(x4.strip())
print x3,"#############", d1
print x4,"##############",  d2
print(abs(int((d2-d1).total_seconds())))

