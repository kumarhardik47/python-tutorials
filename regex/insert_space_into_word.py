import os
import re

s = "HelloHardikHowAreYou?"


out = re.sub(r"(\w)([A-Z])",r"\1 \2",s)
print out
