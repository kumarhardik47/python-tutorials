import os
import re

s = "Mukesh.kumar hello:world hardki@mahto Rajeshwara=>latkhor"

print re.split(' ',s)
print re.split(' |\.',s)
print re.split(' |\.|:',s)
print re.split(' |\.|:|\@',s)
print re.split(' |\.|:|\@|=>',s)
